from django.contrib import admin

from common import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass
