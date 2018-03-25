from django.conf.urls import url, include

from . import views
from .router import weather_router

urlpatterns = [
    url(r'^api/', include(weather_router.urls)),
    url('^upload/?$', views.upload, name='upload'),
    url('^statistics/?$', views.statistics, name='statistics')
]
