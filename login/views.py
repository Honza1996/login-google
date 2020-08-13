from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
import json
from urllib.parse import urlencode
import requests

client_id = "829377338214-beourj0nht178nuv75ih2mg2hekd8s42.apps.googleusercontent.com"
client_secret = "yQjN0Ek1c8cYvYAeiV8cVheH"
redirect_uri = "http://localhost:8000/login/google-login-code"
base_url = r"https://accounts.google.com/o/oauth2/"
authorization_code = ""
access_token = ""
scope = 'https://www.googleapis.com/auth/adwords https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/drive https://www.googleapis.com/auth/content https://www.googleapis.com/auth/analytics'


def post_list(request):
    return render(request, 'login/login.html', {})


def google_login(request):
    url = "{token_request_uri}?response_type={response_type}&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&access_type=offline".format(
        token_request_uri = "https://accounts.google.com/o/oauth2/auth",
        response_type = "code",
        client_id = client_id,
        redirect_uri = redirect_uri,
        scope = scope)
    return HttpResponseRedirect(url)


def google_login_code(request):
    authorization_code = request.GET['code']
    access_token_req = {
        "code": authorization_code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code",
    }
    content_length = len(urlencode(access_token_req))
    access_token_req['content-length'] = str(content_length)

    r = requests.post(base_url + "token", data=access_token_req)
    data = json.loads(r.text)

    request.session['logged'] = 1
    request.session['refresh_token'] = data['refresh_token']

    return HttpResponseRedirect("/dashboard")
