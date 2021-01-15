from django.contrib import admin
from core.models import Evento
# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo','data_evento')
    list_filter = ('titulo','usuario')

admin.site.register(Evento,EventoAdmin)
