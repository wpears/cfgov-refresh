import json

from django.core.management.base import BaseCommand

from v1.models.browse_page import BrowsePage
from v1.tests.wagtail_pages.helpers import publish_changes

class Command(BaseCommand):
    help = 'Monthly updates to data snapshot values'
    # Test/example command:
    # python cfgov/manage.py update_data_snapshot_values --markets="[{'key':'AUT','data_month':'October 2017', 'num_originations': '12345', 'value_originations':'12345', 'year_over_year_change': '12345'}, {'key':'XYZ','data_month':'January 2017', 'num_originations': '123457', 'value_originations':'123457', 'year_over_year_change': '123457'}]"


    def add_arguments(self, parser):
        """Adds all arguments to be processed."""
        parser.add_argument(
            '--snapshot_file',
            nargs='?',
            help='Filename of a JSON file containing all markets\' data snapshot updates'
        )

    def get_data_snapshots(self):
        """ Gets all data snapshots
        Assumes there is one data snapshot per page
        """

        snapshots = []

        for page in BrowsePage.objects.all():
            stream_data = page.specific.content.stream_data
            snapshot = filter(lambda item: item['type'] == 'data_snapshot', stream_data)
            if snapshot:
                snapshot[0]['value']['page'] = page
                snapshots.append(snapshot[0]['value'])

        return snapshots

    def find_data_snapshot(self, market_key, snapshots):
        snapshot = filter(lambda item: item['market_key'] == market_key, snapshots)
        if snapshot:
            return snapshot[0]


    def handle(self, *args, **options):
        # Read markets from file into update dicts
        with open(options['snapshot_file']) as json_data:
            markets = json.load(json_data)

        snapshots = self.get_data_snapshots()
        for market in markets:
            # Look up data snapshot by the provided market key
            snapshot = self.find_data_snapshot(market['key'], snapshots)
            if snapshot:
                # Update snapshot fields with the provided values
                snapshot['data_month'] = market['data_month']
                snapshot['num_originations'] = market['num_originations']
                snapshot['value_originations'] = market['value_originations']
                snapshot['year_over_year_change'] = market['year_over_year_change']

                # Publish changes to the browse page the data snapshot lives on
                page = snapshot['page']
                publish_changes(page.specific)
