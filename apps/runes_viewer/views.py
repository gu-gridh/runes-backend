from gridh_abstract.views import DynamicDepthViewSet

from .models import Runestone
from .serializers import RunestoneSerializer


class MetadataViewSet(DynamicDepthViewSet):
    serializer_class = RunestoneSerializer
    queryset = Runestone.objects.all()


class VennViewSet(DynamicDepthViewSet):
    serializer_class = RunestoneSerializer
    queryset = Runestone.objects.all()