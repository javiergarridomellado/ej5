from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from apu.views import *
from apu.models import Persona
# Create your tests here.Anadido testeo rutas



class PersonaMethodTests(TestCase):

	def test_nombre_persona(self):
		per = Persona(nombre='Jose' ,dni='45678921r',pais='Holanda',equipo='Betis',hobbies='musica', fondo='500')
		per.save()
		self.assertEqual(per.nombre,'Jose')
		self.assertEqual(per.dni,'45678921r')
		self.assertEqual(per.pais,'Holanda')
		self.assertEqual(per.equipo,'Betis')
		self.assertEqual(per.hobbies,'musica')
		self.assertEqual(per.fondo,'500')
		print("Testeo correcto.")


class RutasTests(APITestCase):

	def test_detalle_persona(self):
		per = Persona(nombre='Jose' ,dni='45678921r',pais='Holanda',equipo='Betis',hobbies='musica',fondo='500')
		per.save()
		response = self.client.get('/apu/1/')
		self.assertEqual(response.content,'{"nombre":"Jose","dni":"45678921r","pais":"Holanda","equipo":"Betis","hobbies":"musica","fondo":500}')
		print("Persona consultada en detalle correctamente")

	def test_detalle_varias_personas(self):
		per = Persona(nombre='Jose' ,dni='45678921r',pais='Holanda',equipo='Betis',hobbies='musica',fondo='500')
		per.save()
		per2 = Persona(nombre='Juan' ,dni='55678921r',pais='Espana',equipo='Real',hobbies='skap',fondo='100')
		per2.save()
		response = self.client.get('/apu/')
		self.assertEqual(response.content,'[{"nombre":"Jose","dni":"45678921r","pais":"Holanda","equipo":"Betis","hobbies":"musica","fondo":500},{"nombre":"Juan","dni":"55678921r","pais":"Espana","equipo":"Real","hobbies":"skap","fondo":100}]')
		print("Varias personas consultadas en detalle correctamente")

