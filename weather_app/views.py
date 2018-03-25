from io import BytesIO

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openpyxl import load_workbook

from .models import GeoPosition, WeatherEntry, AverageStats


@csrf_exempt
def upload(request):
    if not request.method == 'POST':
        return HttpResponse()

    wb = load_workbook(filename=BytesIO(request.body))
    lines_gen = wb[wb.sheetnames[0]].values
    titles = lines_gen.next()
    entries = []

    for line in lines_gen:
        entry = dict(zip(titles, line))
        entries.append(entry)

    for entry in entries:
        geoposition, _ = GeoPosition.objects.get_or_create(
            coordinates=entry['geoposition coordinates'],
            height=entry['hight under the ground']
        )

        WeatherEntry.objects.create(
            geoposition=geoposition,
            date=entry['date'],
            time=entry['time'],
            temperature=entry['temperature'],
            wind_speed=entry['wind speed'],
            wind_vector=entry['wind vector direction']
        )

    return HttpResponse('Successfully uploaded %s entries!' % len(entries))


def statistics(request):
    geopositions = GeoPosition.objects.all()
    stats = [
        AverageStats.objects.filter(geoposition=geoposition).latest('datetime')
        for geoposition in geopositions
    ]
    payload = [
        {
            'Coordinates': stat.geoposition.coordinates,
            'Height': stat.geoposition.height,
            'Average temperature': stat.avg_temperature,
            'Average wind speed': stat.avg_wind_speed,
            'Average wind vector': stat.avg_wind_vector,
            'Last update': stat.datetime.strftime("%I:%M%p on %B %d, %Y")
        } for stat in stats
    ]

    return JsonResponse(payload, safe=False)
