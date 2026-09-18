from gridh_abstract.models import DEFAULT_FIELDS, get_fields
from gridh_abstract.serializers import DynamicDepthSerializer

from .models import Runestone


class RunestoneSerializer(DynamicDepthSerializer):

    class Meta:
        model = Runestone
        fields = ['id']+get_fields(Runestone, exclude=DEFAULT_FIELDS + ['coordinates', 'image'])