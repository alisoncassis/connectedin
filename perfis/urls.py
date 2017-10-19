from django.conf.urls import url
from perfis import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^perfis/(?P<perfil_id>[0-9]+)$', views.exibir, name='exibir'),
    url(r'^perfis/(?P<perfil_id>[0-9]+)/convidar$', views.convidar, name='convidar'),
    url(r'^convite/(?P<convite_id>[0-9]+)/aceitar$', views.aceitar, name='aceitar'),
]
