from gridh_abstract.views import DynamicDepthViewSet

from .filters import RunestoneFilter
from .models import Runestone
from .serializers import RunestoneSerializer


class MetadataViewSet(DynamicDepthViewSet):
    serializer_class = RunestoneSerializer
    filterset_fields = None
    filterset_class = RunestoneFilter
    queryset = Runestone.objects.all()


class VennViewSet(DynamicDepthViewSet):
    serializer_class = RunestoneSerializer
    filterset_fields = None
    filterset_class = RunestoneFilter
    queryset = Runestone.objects.all()