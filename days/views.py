import requests

from django.conf import settings
from django.shortcuts import render_to_response


def days(request):
    return render_to_response('days.html')

