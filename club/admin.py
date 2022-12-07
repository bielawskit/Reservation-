from django.contrib import admin

from . import models

admin.site.register(models.Club)
admin.site.register(models.Court)
admin.site.register(models.PriceList)
