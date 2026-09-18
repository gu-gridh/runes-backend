from django_filters import FilterSet
from gridh_abstract.models import DEFAULT_FIELDS, get_fields

from .models import Runestone


class RunestoneFilter(FilterSet):
    class Meta:
        model = Runestone
        fields = ['id'] + get_fields(
            Runestone,
            exclude=DEFAULT_FIELDS + ['coordinates', 'image'],
        )