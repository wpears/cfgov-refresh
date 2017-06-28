from django.core.management.base import BaseCommand

from v1.atomic_elements.organisms import DataSnapshot
from v1.models.base import CFGOVPage


class Command(BaseCommand):
    help = 'Monthly updates to data snapshot values'
    # Test/example command:
    # python cfgov/manage.py update_data_snapshot_values --data_month='July 2017' --market_key='AUT' --num_originations='12345' --value_originations='1245' --year_over_year_change='123'

    def add_arguments(self, parser):
        """Adds all arguments to be processed."""
        parser.add_argument(
            '--data_month',
            nargs='?',
            help='Latest month of data in "month YYYY" form'
        )
        parser.add_argument(
            '--market_key',
            nargs='?',
            help='Three-letter market identifier'
        )
        parser.add_argument(
            '--num_originations',
            nargs='?',
            help='Number of originations'
        )
        parser.add_argument(
            '--value_originations',
            nargs='?',
            help='Dollar value of originations'
        )
        parser.add_argument(
            '--year_over_year_change',
            nargs='?',
            help='Year over year percentage change: positive value followed by "increase" or "decrease"'
        )

    def handle(self, *args, **options):
        # Look up which market to update
        market_key = options['market_key']
        snapshot = self.get_data_snapshot(market_key)
        
        # Update fields with the provided values
        snapshot['data_month'] = options['data_month']
        snapshot['num_originations'] = options['num_originations']
        snapshot['value_originations'] = options['value_originations']
        snapshot['year_over_year_change'] = options['year_over_year_change']

        # Save the updates
        self.update_data_snapshot(snapshot)

    def get_data_snapshot(self, market_key):
        """ Get the data_snapshot object that matches the given market_key.
        Note: This assumes there is only one matching object.
        Returns a dictionary of the matching object's values."""

        snapshots = []

        # Parse through pages to find data_snapshot items
        # This is slow but is only run once per month
        for page in CFGOVPage.objects.all():
            try:
                stream_data = page.specific.content.stream_data
            except:
                continue

            page_snapshot = list(
                filter(lambda item: item['type'] == 'data_snapshot', stream_data))

            if len(page_snapshot) > 0:
                for item in page_snapshot:
                    # Save the page object into the dict so we can find it again
                    item['value']['page_obj'] = page
                    snapshots.append(item['value'])
        
        # Find the matching market_key
        snapshot = filter(lambda item: item['market_key'] == market_key, snapshots)

        if len(snapshot) == 1:
            return snapshot[0]
        elif len(snapshot) > 1:
            # Select first if multiple objects found
            # TODO: Handle more appropriately (warning or error)
            return snapshot[0]
        else:
            return []

    def update_data_snapshot(self, new_snapshot):
        """Save updates to the data_snapshot"""
        page = new_snapshot['page_obj']
        # page.specific.content.stream_data['data_snapshot'] = new_snapshot
        page.save()





