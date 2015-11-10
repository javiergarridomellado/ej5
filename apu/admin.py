from django.contrib import admin
from apu.models import Persona,RegApuesta

class PersonaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'dni', 'pais','equipo','hobbies')
	search_fields = ('nombre', 'dni')

class RegApuestaAdmin(admin.ModelAdmin):
	list_display = ('equipoa', 'equipob', 'capital','apostador','victoria')
	search_fields = ('apostador', 'capital')
	 

admin.site.register(Persona,PersonaAdmin)
admin.site.register(RegApuesta,RegApuestaAdmin)
# Register your models here.
