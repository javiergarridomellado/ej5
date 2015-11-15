from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from apu.views import *
from apu.models import Persona
from django.test.client import RequestFactory
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

#clase para el testeo de rutasss
class RutasTests(APITestCase):

	def test_detalle_persona(self):
		per = Persona(nombre='persona1' ,dni='dni1',pais='pais1',equipo='equipo1',hobbies='hobbies1',fondo='500')
		per.save()
		response = self.client.get('/apu/1/')
		self.assertEqual(response.content,'{"nombre":"persona1","dni":"dni1","pais":"pais1","equipo":"equipo1","hobbies":"hobbies1","fondo":500}')
		print("Persona consultada en detalle correctamente")

	def test_detalle_varias_personas(self):
		per = Persona(nombre='persona1' ,dni='dni1',pais='pais1',equipo='equipo1',hobbies='hobbies1',fondo='500')
		per.save()
		per2 = Persona(nombre='persona2' ,dni='dni2',pais='pais2',equipo='equipo2',hobbies='hobbies2',fondo='500')
		per2.save()
		response = self.client.get('/apu/')
		self.assertEqual(response.content,'[{"nombre":"persona1","dni":"dni1","pais":"pais1","equipo":"equipo1","hobbies":"hobbies1","fondo":500},{"nombre":"persona2","dni":"dni2","pais":"pais2","equipo":"equipo2","hobbies":"hobbies2","fondo":500}]')
		print("Varias personas consultadas en detalle correctamente")

	def test_crea_persona(self):
		"""
			Test para crear una persona
			Metodo post
		"""
		#data={'nombre' : 'persona_post', 'dni' : 'dni_post', 'pais' : 'pais_post', 'equipo' : 'equipo_post', 'hobbies' : 'hobbies_post', 'fondo' : 500}
		data={"nombre":"nombre_post","dni":"dni1","pais":"pais1","equipo":"equipo1","hobbies":"hobbies1","fondo":500}
		response=self.client.post('/apu/',data, format='json')
		self.assertEqual(response.status_code, 201)
		self.assertEqual(Persona.objects.get().nombre,'nombre_post')
		print("REST: Persona Creada correctamente")
	
	def test_actualiza_persona(self):
		"""
			Test para actualizar una persona
			Metodo post
		"""
		per = Persona(nombre='Jose' ,dni='45678921r',pais='Holanda',equipo='Betis',hobbies='musica',fondo='500')
		per.save()
		data={"nombre":"nombre_update","dni":"dni1","pais":"pais1","equipo":"equipo1","hobbies":"hobbies1","fondo":500}
		#data={'nombre':'nombre_update','dni':'dni_update','pais':'pais1','equipo':'equipo1','hobbies':'hobbies1','fondo':500}
		response=self.client.post('/apu/1/',data, format='json')
		#response=self.client.post('/apu/1/',data, format='json')
		self.assertEqual(Persona.objects.get().nombre, 'nombre_update')
		#self.assertEqual(Persona.objects.get().dni, 'dni_update')
		self.assertEqual(response.status_code, 202)
        print("REST: Persona actualizada correctamente")

	def test_borra_persona(self):
		"""
			Test para borrar una persona
		 	Delete
		"""
		per = Persona(nombre='Jose' ,dni='45678921r',pais='Holanda',equipo='Betis',hobbies='musica',fondo='500')
		per.save()
		response=self.client.delete('/apu/1/',pk=per.nombre)
		self.assertEqual(response.status_code, 204)
        print("REST: Persona borrada correctamente")
