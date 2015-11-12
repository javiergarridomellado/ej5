from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from apu.models import Persona
from django.views.generic import CreateView, TemplateView, ListView
import datetime
from django.views import generic
from django.core.mail import send_mail 



from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from apu.models import Persona
from apu.serializers import PersonaSerializer




# Create your views here.
def raiz(request):
	"""Funcion que da la hora actual
	"""
	ahora = datetime.datetime.now()
	return render(request,'indice.html',{'fecha_actual':ahora})

def mostrar_navegador(request):
	"""Muestra navegador usado
	"""
	try:
		ua = request.META['HTTP_USER_AGENT']
	except KeyError:
		ua = 'unknown'
	return HttpResponse("Tu navegador es %s" % ua) 
	
def formulario_buscar(request):
	"""Busca persona en la base datos
	"""
	return render(request,'formulario_buscar.html')



class RegistrarUsuario(CreateView):
	"""No funciona corregir
	"""
	model = Persona
	template_name = 'registrarusuario.html'
	
	#success_url = reverse_lazy('redirigir_empresa')

class RedirigirUsuario(ListView):
	"""No funciona, corregir
	"""
	template_name = 'redirigirusuario.html'
	model = Persona
	context_object_name = 'personas'

def buscarr(request): 
 
    if 'dni' in request.GET and 'nombre' in request.GET and request.GET['dni'] and request.GET['nombre']: 
        mensaje = 'Estas buscando a %r ' %request.GET['nombre'] + 'con DNI: %r ' %  request.GET['dni'] 
    else: 
        mensaje = 'Haz subido un formulario vacio.' 
    return HttpResponse(mensaje)

def buscar(request):
	"""Busca personas segun parametros GET
	"""
	error=False
	if 'dni' in request.GET:
		dni = request.GET['dni']
		if not dni:
			error=True
		else:
			personas = Persona.objects.filter(dni__icontains=dni)
			return render(request,'resultados.html',  {'personas': personas, 'query': dni})
	
	return render(request, 'formulario_buscar.html', {'error': error})
		#return HttpResponse('Por favor introduce un termino de busqueda.') 

def contactos(request):
	errors=[]
	if request.method=='POST':
		if not request.POST.get('asunto', ''):
			errors.append('Por favor introduce el asunto.')
		if not request.POST.get('mensaje', ''):
			errors.append('Por favor introduce un mensaje.')
		if request.POST.get('email') and '@' not in request.POST['email']:
			errors.append('Por favor introduce una direccion email valida')
		if not errors:
			#configurar serv correo
			#send_mail(request.POST['asunto'], request.POST['mensaje'], request.POST.get('email', 'noreply@example.com'), ['siteowner@example.com'], )
			return HttpResponseRedirect('/contactos/gracias/')
	return render(request, 'formulario_contactos.html',{'errors':errors,'asunto':request.POST.get('asunto', ''),'mensaje':request.POST.get('mensaje', ''),'email':request.POST.get('email', '')})

def gracias_contactos(request):
	mensaje = 'Gracias por ponerte en contacto con nosotros, su propuesta sera tenida en cuenta.'
	return HttpResponse(mensaje)


class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON.
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def Persona_lista(request):
	"""
	Lista todos los nombres de personas o la crea
	"""
	if request.method == 'GET':
		personas = Persona.objects.all()
		serializador = PersonaSerializer(personas, many=True)
		return JSONResponse(serializador.data)
	
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializador = PersonaSerializer(data=data)
		if serializador.is_valid():
			serializador.save()
			return JSONResponse(serializador.data, status=201)
		return JSONResponse(serializador.errors, status=400)

@csrf_exempt
def Persona_detalle(request, pk):
	"""
	Recuperar, actualizar o borrar una persona
	"""
	try:
		persona = Persona.objects.get(pk=pk)
	except Persona.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializador = PersonaSerializer(persona)
		return JSONResponse(serializador.data)
	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializador = PersonaSerializer(persona, data=data)
		if serializador.is_valid():
			serializador.save()
			return JSONResponse(serializador.data,status=202)
		return JSONResponse(serializador.errors, status=400)
	elif request.method == 'DELETE':
		persona.delete()
		return HttpResponse(status=204)
