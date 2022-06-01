from django.contrib import admin
from .models import GeeksModel, Event
from .views import export_data
# Register your models here.

@admin.register(GeeksModel)
class GeeksModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'biography')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    actions = [export_data]
    list_display = ('name', 'event_date', 'venue', 'manager', 'description')
