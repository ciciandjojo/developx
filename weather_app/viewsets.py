from rest_framework.viewsets import ModelViewSet

from .models import GeoPosition, WeatherEntry, AverageStats
from .serializers import (
    GeoPositionSerializer, WeatherEntrySerializer, AverageStatsSerializer
)


class GeoPositionAPI(ModelViewSet):
    queryset = GeoPosition.objects.all()
    serializer_class = GeoPositionSerializer


class WeatherEntryAPI(ModelViewSet):
    queryset = WeatherEntry.objects.all()
    serializer_class = WeatherEntrySerializer


class AverageStatsAPI(ModelViewSet):
    queryset = AverageStats.objects.all()
    serializer_class = AverageStatsSerializer
