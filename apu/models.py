from django.db import models
#Para generar la documentacion ejecutar epydoc --html views.py models.py (sale error pero genera los html)
# Create your models here.

class Persona(models.Model):
	"""Modelo del registro Persona.
		Nombre -> Nombre del Usuario, tipo char maxlenght 50
		Apellidos -> Apellido del Usuario, tipo char maxlenght 100
		dni -> Documento Nacional,tipo char maxlenght 9
		equipo -> Seguidor de equipo, tipo char maxlenght 10
		pais -> tipo char maxlenght 20
		hobbies -> tipo textfield		
	"""

	nombre = models.CharField(max_length=50)
	dni = models.CharField(max_length=9)
	pais = models.CharField(max_length=20)
	equipo = models.CharField(max_length=10)
	hobbies = models.TextField(max_length=200)
	#password = models.PasswordField(max_length=15)
	fondo = models.IntegerField()

	def __unicode__(self):
		return self.nombre

class RegApuesta(models.Model):
	"""Modelo del registro Apuesta.
		#Nombre -> tipo char maxlenght 50
		#Apellidos -> tipo char maxlenght 100
		#dni -> tipo char maxlenght 9
		#pais -> tipo char maxlenght 20
		#hobbies -> tipo textfield		
	"""
	equipoa = models.CharField(max_length=50)
	equipob = models.CharField(max_length=50)
	capital = models.IntegerField()
	apostador = models.ForeignKey(Persona)
	victoria = models.CharField(max_length=1)

	def __unicode__(self):
		return '%s -  %s resultado: %s' %(self.equipoa, self.equipob,self.victoria)
 
	

	
