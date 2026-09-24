from gridh_abstract.views import DynamicDepthViewSet
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .filters import RunestoneFilter
from .models import Runestone, TimePeriod, Area
from .serializers import RunestoneSerializer, VennSerializer


class MetadataViewSet(DynamicDepthViewSet):
    serializer_class = RunestoneSerializer
    filterset_fields = None
    filterset_class = RunestoneFilter
    queryset = Runestone.objects.all()


class VennViewSet(ViewSet):
    queryset = Runestone.objects.all()

    def list(self, request):
        areas = Area.objects.all()
        periods = TimePeriod.objects.all()

        runestones = (
            Runestone.objects
            .select_related("place__area", "time_period")
            .prefetch_related("runestoneposition_set__position")
        )

        data = {
            area.text: {
                **{
                    period.text: {
                        "venn": [],
                        "outside": [],
                    }
                    for period in periods
                },
                "unknown": {
                    "venn": [],
                    "outside": [],
                },
            }
            for area in areas
        }

        for runestone in runestones:
            serialized = VennSerializer(runestone).data

            area = runestone.place.area.text
            time_period = runestone.time_period.text if runestone.time_period else "unknown"

            if not serialized["sets"]:
                data[area][time_period]["outside"].append({"id": runestone.id,
                                                           "name": runestone.name})
                continue

            data[area][time_period]["venn"].append(serialized)

        return Response(data)
