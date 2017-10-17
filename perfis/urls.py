from django.conf.urls import url
from perfis.views import index, exibir

urlpatterns = [
    url(r'^$', index, name = 'index'),
    url(r'^perfis/(?P<perfil_id>[0-9]+)$', exibir, name = 'exibir'),
]
