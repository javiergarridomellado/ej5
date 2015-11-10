from rest_framework import serializers
from apu.models import Persona


class PersonaSerializer(serializers.Serializer):
	nombre = serializers.CharField(max_length=50)
	dni = serializers.CharField(max_length=9)
	pais = serializers.CharField(max_length=20)
	equipo = serializers.CharField(max_length=10)
	hobbies = serializers.CharField(max_length=200)
	fondo = serializers.IntegerField()
	
	def create(self, validated_data):
		"""
		Creacion y return de una nueva instancia de Persona
		"""
		return Persona.objects.create(**validated_data)

	def update(self, instance, validated_data):
		"""
		Actualizacion y return de una instancia de Persona ya existente con los datos validados
		"""
		instance.nombre = validated_data.get('nombre', instance.nombre)
		instance.dni = validated_data.get('dni', instance.dni)
		instance.pais = validated_data.get('pais', instance.pais)
		instance.equipo = validated_data.get('equipo', instance.equipo)
		instance.hobbies = validated_data.get('hobbies', instance.hobbies)
		instance.fondo = validated_data.get('fondo', instance.fondo)
		instance.save()
		return instance

