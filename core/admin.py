from django.contrib import admin

# Register your models here.
from core import models
@admin.register(models.MessengerBelayer)
class MessengerBelayerAdmin(admin.ModelAdmin):
    pass
