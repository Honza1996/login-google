from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'', views.dashboard, name='dashboard'),
     # url(r'google-login-code/', views.google_login_code, name='google_login_code'),
]
