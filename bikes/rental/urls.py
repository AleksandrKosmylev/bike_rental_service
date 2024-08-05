from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from bikes.rental import views
from .views import Home


urlpatterns = [
    # path('', views.apt_root),
    path('', Home.as_view()),
    path('bikes/', views.BikesList.as_view(), name='bikes-list'),

]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['html'])



