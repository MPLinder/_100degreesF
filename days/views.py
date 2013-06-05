import datetime
import requests

from django.conf import settings
from django.shortcuts import render_to_response

from days.models import Day, City


def days(request):
    city = request.GET.get('city', 'Austin')
    # TODO: cities may have the same name
    city = City.objects.get(name=city)

    year = request.GET.get('year', datetime.datetime.today().year)

    days = Day.objects.filter(date__year=year, city=city)
    days = dict([(day.date, day.temp) for day in days])

    context = {
        'city': city.name,
        'state': city.state.name,
        'country': city.state.country.name,
        'year': year,
        'days': days,
    }

    # TODO: keeping this code to put in the script
    # url = settings.WUNDERGROUND_API_URL + '/' + settings.WUNDERGROUND_API_KEY + '/' + 'history_20120804/q/TX/Austin.json'
    # r = requests.get(url)
    # temp = r.json()['history']['dailysummary'][0]['maxtempi']
    return render_to_response('days.html', context)

