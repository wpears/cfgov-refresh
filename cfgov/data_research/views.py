from __future__ import unicode_literals
import datetime

from haystack.query import SearchQuerySet
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from data_research.models import (
    County, CountyMortgageData,
    MetroArea, MSAMortgageData, NonMSAMortgageData,
    State, StateMortgageData,
    MortgageMetaData, NationalMortgageData)

DAYS_LATE_RANGE = ['30-89', '90']


class MetaData(APIView):
    """
    View for delivering mortgage metadata based on latest data update.
    """
    renderer_classes = (JSONRenderer,)

    def get(self, request, meta_name):
        try:
            record = MortgageMetaData.objects.get(name=meta_name)
        except MortgageMetaData.DoesNotExist:
            return Response("No metadata object found.")
        meta_json = record.json_value
        return Response(meta_json)


class TimeSeriesNational(APIView):
    """
    View for delivering national time-series data
    from the mortgage performance dataset.
    """
    renderer_classes = (JSONRenderer,)  # , rfc_renderers.CSVRenderer)

    def get(self, request, days_late):
        if days_late not in DAYS_LATE_RANGE:
            return Response("Unknown delinquency range")
        records = NationalMortgageData.objects.all()
        data = {'meta': {'name': 'United States',
                         'fips_type': 'national'},
                'data': [record.time_series(days_late)
                         for record in records]}
        return Response(data)


class TimeSeriesData(APIView):
    """
    View for delivering geo-based time-series data
    from the mortgage performance dataset.
    """
    renderer_classes = (JSONRenderer,)

    def get(self, request, days_late, fips):
        """
        Return a FIPS-based slice of base data as a json timeseries.
        """
        if days_late not in DAYS_LATE_RANGE:
            return Response("Unknown delinquency range")
        reference_lists = {
            entry: MortgageMetaData.objects.get(name=entry).json_value
            for entry in ['whitelist', 'msa_fips', 'non_msa_fips']}
        if fips not in reference_lists['whitelist']:
            return Response("FIPS code not found or not valid.")
        if len(fips) == 2:
            state = State.objects.get(fips=fips)
            records = StateMortgageData.objects.filter(
                fips=fips)
            data = {'meta': {'fips': fips,
                             'name': state.name,
                             'fips_type': 'state'},
                    'data': [record.time_series(days_late)
                             for record in records]}
            return Response(data)
        if 'non' in fips:
            records = NonMSAMortgageData.objects.filter(
                fips=fips)
            data = {'meta': {'fips': fips,
                             'name': "Non-metro area of {}".format(
                                 records.first().state.name),
                             'fips_type': 'non_msa'},
                    'data': [record.time_series(days_late)
                             for record in records]}
            return Response(data)

        if fips in reference_lists['msa_fips']:
            metro_area = MetroArea.objects.get(fips=fips, valid=True)
            records = MSAMortgageData.objects.filter(fips=fips)
            data = {'meta': {'fips': fips,
                             'name': metro_area.name,
                             'fips_type': 'msa'},
                    'data': [record.time_series(days_late)
                             for record in records]}
            return Response(data)
        else:  # must be a county request
            try:
                county = County.objects.get(fips=fips, valid=True)
            except County.DoesNotExist:
                return Response("County is below display threshold.")
            records = CountyMortgageData.objects.filter(fips=fips)
            name = "{}, {}".format(county.name, county.state.abbr)
            data = {'meta': {'fips': fips,
                             'name': name,
                             'fips_type': 'county'},
                    'data': [record.time_series(days_late)
                             for record in records]}
        return Response(data)


def validate_year_month(year_month):
    """Trap non-integers, malformatted entries, and out-of-range dates."""

    current_year = datetime.date.today().year
    split = year_month.split('-')
    if len(split) != 2:
        return None
    try:
        year = int(split[0])
        month = int(split[1])
    except ValueError:
        return None
    if year > current_year or month not in range(1, 13):
        return None
    if year < 1998:
        return None
    return datetime.date(year, month, 1)


def update_map_payload(records, geo, geo_dict, days_late, payload):
    """
    Update a metro or county payload via Elasticsearch, falling back to
    a slower database query if Elasticsearch is not available.
    """
    def map_value(record, days_late):
        record_dict = {
            '90': record.percent_90,
            '30-89': record.percent_30_60}
        return record_dict[days_late]

    if len(records) > 0:  # Elasticsearch is responding # pragma: no cover
        for record in records:
            map_values = {'value': map_value(record, days_late),
                          'name': record.name}
            payload['data'].update({record.fips: map_values})
        return payload
    # No Elasticsearch, so we fall back to database queries
    records = geo_dict[geo]['fallback_queryset']
    for record in records:
        geo_parent = getattr(record, geo_dict[geo]['fips_type'])
        if geo == 'counties':
            name = "{}, {}".format(
                geo_parent.name, geo_parent.state.abbr)
        else:
            name = geo_parent.name
        map_values = {'name': name}
        if geo_parent.valid is True:
            map_values['value'] = map_value(record, days_late)
        else:
            map_values['value'] = None
        payload['data'].update({record.fips: map_values})
    return payload


class MapData(APIView):
    """
    View for delivering geo-based map data by date
    from the mortgage performance dataset.
    """
    renderer_classes = (JSONRenderer,)

    def get(self, request, days_late, geo, year_month):
        date = validate_year_month(year_month)
        if date is None:
            return Response("Invalid year-month pair")
        if days_late not in DAYS_LATE_RANGE:
            return Response("Unknown delinquency range")
        geo_dict = {
            'national':
                {'queryset': NationalMortgageData.objects.get(date=date),
                 'fallback_queryset': [],
                 'fips_type': 'nation'},
            'states':
                {'queryset': StateMortgageData.objects.filter(date=date),
                 'fallback_queryset': [],
                 'fips_type': 'state'},
            'counties':
                {'queryset':
                 SearchQuerySet().models(CountyMortgageData).filter(
                     content=date.strftime("%Y%m%d")),
                 'fallback_queryset': CountyMortgageData.objects.filter(
                     date=date, county__valid=True),
                 'fips_type': 'county'},
            'metros':
                {'queryset':
                 SearchQuerySet().models(MSAMortgageData).filter(
                     content=date.strftime("%Y%m%d")),
                 'fallback_queryset': MSAMortgageData.objects.filter(
                     date=date),
                 'fips_type': 'msa'},
        }
        if geo not in geo_dict:
            return Response("Unkown geographic unit")
        payload = {'meta': {'fips_type': geo_dict[geo]['fips_type'],
                            'date': '{}'.format(date)},
                   'data': {}}
        nat_record = geo_dict['national']['queryset']
        nat_data_series = {
            'name': 'United States',
            'value': nat_record.time_series(days_late)['value']}
        if geo == 'national':
            payload['data'] = nat_data_series
            return Response(payload)
        payload['meta']['national_average'] = nat_data_series['value']
        records = geo_dict[geo]['queryset']
        if geo == 'states':
            for record in records:
                data_series = {
                    'name': record.state.name,
                    'value': record.time_series(days_late)['value']}
                payload['data'].update({record.fips: data_series})
            return Response(payload)
        # geo is now either county or metro, so we want Elasticsearch
        payload = update_map_payload(
            records, geo, geo_dict, days_late, payload)
        if geo == 'metros':  # map needs metro and non-metro data together
            for non in NonMSAMortgageData.objects.filter(date=date):
                non_name = "Non-metro area of {}".format(non.state.name)
                non_data_series = {'name': non_name}
                if non.state.non_msa_valid is True:
                    non_data_series['value'] = non.time_series(
                        days_late)['value']
                else:
                    non_data_series['value'] = None
                payload['data'].update({non.fips: non_data_series})
        return Response(payload)
