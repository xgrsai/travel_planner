from django.contrib import admin

from travel import models


admin.site.register(models.TravelProject)
admin.site.register(models.Place)