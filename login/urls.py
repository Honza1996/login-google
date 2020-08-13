from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'google-login/', views.google_login, name='google_login'),
     url(r'google-login-code/', views.google_login_code, name='google_login_code'),
]
