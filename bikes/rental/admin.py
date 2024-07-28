from django.contrib import admin
from bikes.rental.models import Bikes
from bikes.users.models import CustomUser


# Register your models here.
admin.site.register(Bikes)
admin.site.register(CustomUser)