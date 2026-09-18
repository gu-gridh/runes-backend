from gridh_abstract.models import DEFAULT_FIELDS, get_fields
from gridh_abstract.serializers import DynamicDepthSerializer
from rest_framework import serializers

from .models import Runestone, RunestonePosition


class RunestoneSerializer(DynamicDepthSerializer):

    class Meta:
        model = Runestone
        fields = ['id']+get_fields(Runestone, exclude=DEFAULT_FIELDS + ['coordinates', 'image'])


class VennSerializer(serializers.ModelSerializer):
    sets = serializers.SerializerMethodField()

    class Meta:
        model = Runestone
        fields = ["id", "sets", "name"]

    def get_sets(self, obj):
        allowed_positions = {
            "Väg": "Väg",
            "Grav": "Grav",
            "Gräns": "Gräns",
        }

        positions = obj.runestoneposition_set.filter(
            status=RunestonePosition.Status.YES,
            position__text__in=allowed_positions.keys(),
        ).select_related("position")

        return [
            allowed_positions[item.position.text]
            for item in positions
        ]
