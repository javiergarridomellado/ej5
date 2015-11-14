from django import forms
from apu.models import Persona

class FormularioContactos(forms.Form):
	asunto=forms.CharField()
	email=forms.EmailField(required=False)
	mensaje=forms.CharField()

class PersonaForm(forms.ModelForm):
	nombre = forms.CharField(max_length=50,help_text="nombre Persona")
	dni = forms.CharField(max_length=9,help_text="dni Persona")
	pais = forms.CharField(max_length=20,help_text="pais Persona")
	equipo = forms.CharField(max_length=10,help_text="equipo Persona")
	hobbies = forms.TextField(max_length=200,help_text="hobbies Persona")
	#password = models.PasswordField(max_length=15)
	fondo = forms.IntegerField()
    class Meta:
        model = Persona
        fields = ('nombre','dni','pais','equipo','hobbies','fondo')
