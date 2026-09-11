from gridh_abstract.views import DynamicDepthViewSet

from runes_viewer.models import Runestone
from runes_viewer.serializers import RunestoneSerializer


class MetadataViewSet(DynamicDepthViewSet):
    serializer_class = RunestoneSerializer
    queryset = Runestone.objects.all()


class VennViewSet(DynamicDepthViewSet):
    serializer_class = RunestoneSerializer
    queryset = Runestone.objects.all()