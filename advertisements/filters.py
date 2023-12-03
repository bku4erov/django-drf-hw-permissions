from django_filters import rest_framework as filters
from django.contrib.auth import get_user_model

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    # status = filters.ChoiceFilter(choices=AdvertisementStatusChoices)
    created_at = filters.DateFromToRangeFilter()
    # creator = filters.ModelChoiceFilter(queryset=get_user_model().objects.all())

    class Meta:
        model = Advertisement
        fields = ['created_at']
        # fields = ['title', 'description', 'creator',
        #           'status', 'created_at']
