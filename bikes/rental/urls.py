from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from bikes.rental import views


urlpatterns = [
    # path('', views.apt_root),
    path('bikes/', views.BikesList.as_view(), name='bikes-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['html'])
