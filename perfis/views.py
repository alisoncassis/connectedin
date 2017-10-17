# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):
    return render(request, 'perfil.html', {'perfil' : Perfil.objects.get(id=perfil_id)})
