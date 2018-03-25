from django.db import models


class GeoPosition(models.Model):
    coordinates = models.CharField(max_length=255)
    height = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return u'{} : {}'.format(self.coordinates, self.height)


class WeatherEntry(models.Model):
    geoposition = models.ForeignKey(GeoPosition)
    date = models.DateField()
    time = models.TimeField()
    temperature = models.FloatField()
    wind_speed = models.FloatField()
    wind_vector = models.FloatField()


class AverageStats(models.Model):
    geoposition = models.ForeignKey(GeoPosition)
    datetime = models.DateTimeField()
    avg_temperature = models.FloatField()
    avg_wind_speed = models.FloatField()
    avg_wind_vector = models.FloatField()
