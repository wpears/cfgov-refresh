from __future__ import unicode_literals

# import json

from haystack import indexes

from data_research.models import CountyMortgageData, MSAMortgageData


class CountyMortgageDataIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True)
    fips = indexes.CharField(model_attr='fips')
    date = indexes.DateField(model_attr='date')
    name = indexes.CharField()
    percent_30_60 = indexes.FloatField(model_attr='percent_30_60')
    percent_90 = indexes.FloatField(model_attr='percent_90')

    def prepare_text(self, obj):
        return obj.date.strftime('%Y%m%d')

    def prepare_name(self, obj):
        return "{}, {}".format(obj.county.name, obj.county.state.abbr)

    def get_model(self):
        return CountyMortgageData

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(county__valid=True)


class MSAMortgageDataIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True)
    fips = indexes.CharField(model_attr='fips')
    date = indexes.DateField(model_attr='date')
    name = indexes.CharField(model_attr='msa__name')
    percent_30_60 = indexes.FloatField(null=True)
    percent_90 = indexes.FloatField(null=True)
    valid = indexes.BooleanField(model_attr='msa__valid')

    def prepare_text(self, obj):
        return obj.date.strftime('%Y%m%d')

    def prepare_percent_30_60(self, obj):
        if obj.msa.valid is False:
            return None
        return obj.percent_30_60

    def prepare_percent_90(self, obj):
        if obj.msa.valid is False:
            return None
        return obj.percent_90

    def get_model(self):
        return MSAMortgageData

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
