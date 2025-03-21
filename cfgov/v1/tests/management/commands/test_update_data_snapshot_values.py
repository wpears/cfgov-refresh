import os

from django.conf import settings
from django.core.management import call_command
from django.test import TestCase

from wagtail.blocks import StreamValue

from scripts import _atomic_helpers as atomic
from v1.models.browse_page import BrowsePage
from v1.models.sublanding_page import SublandingPage
from v1.tests.wagtail_pages.helpers import publish_page


class UpdateDataSnapshotValuesTestCase(TestCase):
    def test_data_snapshot(self):
        """Management command correctly updates data snapshot values"""
        browse_page = BrowsePage(title="Browse Page", slug="browse")
        sl = SublandingPage(title="Consumer Credit Trends", slug="cct")

        # Adds a STU market to a browse page
        browse_page.content = StreamValue(
            browse_page.content.stream_block, [atomic.data_snapshot], True
        )

        sl.content = StreamValue(
            sl.content.stream_block, [atomic.full_width_text], True
        )

        publish_page(child=browse_page)
        publish_page(child=sl)

        # Call management command to update values
        filename = os.path.join(
            settings.PROJECT_ROOT, "v1/tests/fixtures/data_snapshot.json"
        )
        call_command(
            "update_data_snapshot_values",
            f"--snapshot_file={filename}",
        )
        response = self.client.get("/browse/")

        # July 2018 data:
        # Student loans originated
        self.assertContains(response, "917,007")
        # Dollar volume of new loans
        self.assertContains(response, "$16.6 billion")
        # In year-over-year originations
        self.assertContains(response, "48.0% increase")
        self.assertContains(response, "July&nbsp;2018")
        self.assertContains(response, "Loans originated")
        self.assertContains(response, "Dollar value of new loans")
        self.assertContains(response, "In year-over-year originations")
        # Should not contain inquiry and tightness values
        self.assertNotContains(response, "In year-over-year inquiries")
        self.assertNotContains(response, "In year-over-year credit tightness")

        landing_response = self.client.get("/cct/")
        self.assertContains(landing_response, "October 02, 2018")

    def test_data_snapshot_with_inquiry_and_tightness(self):
        """Management command correctly updates data snapshot values
        for market that contains inquiry and tightness data"""
        browse_page = BrowsePage(
            title="Browse Page",
            slug="browse",
        )

        sl = SublandingPage(title="Consumer Credit Trends", slug="cct")

        # Adds a AUT market to a browse page
        browse_page.content = StreamValue(
            browse_page.content.stream_block,
            [atomic.data_snapshot_with_optional_fields],
            True,
        )

        sl.content = StreamValue(
            sl.content.stream_block, [atomic.full_width_text], True
        )

        publish_page(child=browse_page)
        publish_page(child=sl)

        # Call management command to update values
        filename = os.path.join(
            settings.PROJECT_ROOT, "v1/tests/fixtures/data_snapshot.json"
        )
        call_command(
            "update_data_snapshot_values",
            f"--snapshot_file={filename}",
        )
        # July 2018
        response = self.client.get("/browse/")
        # Auto loans originated
        self.assertContains(response, "2.5 million")
        # Dollar volume of new loans
        self.assertContains(response, "$54.6 billion")
        # In year-over-year originations
        self.assertContains(response, "7.3% increase")
        self.assertContains(response, "July&nbsp;2018")
        self.assertContains(response, "Loans originated")
        self.assertContains(response, "Dollar value of new loans")
        self.assertContains(response, "In year-over-year originations")
        # Inquiry and tightness values
        self.assertContains(response, "7.9% increase")
        self.assertContains(response, "2.8% increase")
        self.assertContains(response, "In year-over-year inquiries")
        self.assertContains(response, "In year-over-year credit tightness")
