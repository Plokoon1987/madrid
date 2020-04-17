from django.contrib import admin
from . import models

@admin.register(models.Estacion)
class EstacionAdmin(admin.ModelAdmin):
    list_display = ('provincia', 'municipio', 'estacion')

@admin.register(models.DiaMedicion)
class DiaMedicionAdmin(admin.ModelAdmin):
    list_display = ('estacion', 'ano', 'mes', 'dia', 'magnitud', 'punto_muestreo')

@admin.register(models.HoraMedicion)
class HoraMedicionAdmin(admin.ModelAdmin):
    list_display = ('dia_medicion', 'hora', 'cantidad', 'validacion')
    list_filter = ('validacion', 'hora')
