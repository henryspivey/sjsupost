import datetime
from haystack import indexes
from classifieds.models import model_for_individual_listing


class ListingIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    listing_name = indexes.CharField(model_attr='title')

    def get_model(self):
        return model_for_individual_listing

    """def index_queryset(self, using=None):
                    return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())"""