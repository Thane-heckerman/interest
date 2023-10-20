from django.contrib import admin
from .models import History ,StatusTracking
# Register your models here.

admin.site.register(History.History)
admin.site.register(StatusTracking.StatusTracking)