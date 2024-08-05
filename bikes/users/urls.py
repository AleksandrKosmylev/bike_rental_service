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

from .views import UserList
from .views import UserDetail

urlpatterns = [
    re_path(r'^registration/?$', UserList.as_view(), name='user_registration'),
    re_path(r'^login/?$', UserDetail.as_view(), name='user_login'),
]