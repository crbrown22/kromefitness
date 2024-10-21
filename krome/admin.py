from django.contrib import admin
from . models import Athlete
from django.contrib.auth.models import Group

# Register your models here.
admin.site.site_header = 'KROME Fitness'



admin.site.register(Athlete)
