from gridh_abstract.models import DEFAULT_FIELDS, get_fields
from gridh_abstract.serializers import DynamicDepthSerializer
from rest_framework_gis.serializers import GeoModelSerializer
from rest_framework import serializers

from .models import Position, Runestone, RunestonePosition, TimePeriod


class TimePeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimePeriod
        fields = ('id', 'text')


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'text')


class RunestonePositionSerializer(serializers.ModelSerializer):
    position = PositionSerializer()

    class Meta:
        model = RunestonePosition
        fields = ["position", "status"]


class RunestoneSerializer(DynamicDepthSerializer):
    time_period = TimePeriodSerializer()
    positions = RunestonePositionSerializer(
        source="runestoneposition_set",
        many=True,
        read_only=True,
    )
    longitude = serializers.SerializerMethodField()
    latitude = serializers.SerializerMethodField()

    def get_longitude(self, obj):
        return obj.coordinates.x if obj.coordinates else None

    def get_latitude(self, obj):
        return obj.coordinates.y if obj.coordinates else None

    class Meta:
        model = Runestone
        fields = ['id', 'positions', 'longitude', 'latitude']+get_fields(Runestone, exclude=DEFAULT_FIELDS + ['image', 'position'])


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
