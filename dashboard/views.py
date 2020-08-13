from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
import json
from urllib.parse import urlencode
import requests


def dashboard(request):
    login = request.session['logged']
    refresh_token = request.session['refresh_token']
    return render(request, 'dashboard/index.html', {'login': login, 'refresh_token': refresh_token})
