from datetime import datetime as dt

from celery import shared_task
from django.utils import timezone

from .models import GeoPosition, WeatherEntry, AverageStats


@shared_task
def calculate_average():
    for geoposition in GeoPosition.objects.all():
        entries = WeatherEntry.objects.filter(geoposition=geoposition)
        latest_datetime = dt.combine(
            entries.first().date, entries.first().time)
        temperatures = []
        wind_speeds = []
        wind_vectors = []

        for entry in entries:
            datetime = dt.combine(entry.date, entry.time)
            if datetime > latest_datetime:
                latest_datetime = datetime
            temperatures.append(entry.temperature)
            wind_speeds.append(entry.wind_speed)
            wind_vectors.append(entry.wind_vector)

        latest_datetime = timezone.make_aware(latest_datetime,
                                              timezone.get_current_timezone())

        AverageStats.objects.get_or_create(
            geoposition=geoposition,
            datetime=latest_datetime,
            avg_temperature=sum(temperatures)/len(temperatures),
            avg_wind_speed=sum(wind_speeds)/len(wind_speeds),
            avg_wind_vector=sum(wind_vectors)/len(wind_vectors),
        )
