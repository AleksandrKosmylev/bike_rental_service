"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from bikes.users import views


urlpatterns = [
    # path('', views.apt_root),
    path('', views.UserList.as_view(), name='user-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['html'])
"""
from django.urls import re_path

from .views import RegistrationAPIView
from .views import LoginAPIView

urlpatterns = [
    re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
]