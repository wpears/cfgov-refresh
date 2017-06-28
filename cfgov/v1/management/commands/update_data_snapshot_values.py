from django.core.management.base import BaseCommand

from v1.models.browse_page import BrowsePage
from v1.tests.wagtail_pages.helpers import publish_changes

class Command(BaseCommand):
    help = 'Monthly updates to data snapshot values'
    # Test/example command:
    # python cfgov/manage.py update_data_snapshot_values --data_month='September 2017' --market_key='AUT' --num_originations='12345' --value_originations='1245' --year_over_year_change='123'

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

    def find_data_snapshot(self, market_key):
        snapshots = self.get_data_snapshots()
        snapshot = filter(lambda item: item['market_key'] == market_key, snapshots)
        if snapshot:
            return snapshot[0]


    def handle(self, *args, **options):
        # Look up data snapshot by the provided market key
        snapshot = self.find_data_snapshot(options['market_key'])
        
        # Update snapshot fields with the provided values
        snapshot['data_month'] = options['data_month']
        snapshot['num_originations'] = options['num_originations']
        snapshot['value_originations'] = options['value_originations']
        snapshot['year_over_year_change'] = options['year_over_year_change']

        # Publish changes to the browse page the data snapshot lives on
        page = snapshot['page']
        publish_changes(page.specific)



