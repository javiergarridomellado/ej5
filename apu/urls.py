from django.conf.urls import url
from django.conf.urls import patterns, include

from . import views
from apu.views import raiz, mostrar_navegador, contactos, gracias_contactos


# Serializers define the API representation.
#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Persona
#        fields = ('nombre', 'dni')

# ViewSets define the view behavior.
#class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
#router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)
urlpatterns = [
	url(r'^$', raiz),
	url(r'^navegador/$' ,mostrar_navegador),
	url(r'^registrarusuario/$' , views.RegistrarUsuario.as_view() , name="registrar_usuario" ),
	url(r'^formulariobuscar/$', views.formulario_buscar),
	url(r'^buscar/$', views.buscar),
	url(r'^contactos/$', contactos),
	url(r'^contactos/gracias/$', gracias_contactos),
	url(r'^apu/$', views.Persona_lista),
    url(r'^apu/(?P<pk>[0-9]+)/$', views.Persona_detalle),

]
#url(r'^$', views.IndexView.as_view(), name='index'),
