from rest_framework.routers import DefaultRouter
from .viewsets import (
    GeoPositionAPI, WeatherEntryAPI, AverageStatsAPI
)

weather_router = DefaultRouter()

weather_router.register('geoposition', GeoPositionAPI)
weather_router.register('weather-entry', WeatherEntryAPI)
weather_router.register('average-stats', AverageStatsAPI)
