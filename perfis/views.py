# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):
    perfil = Perfil()
    if perfil_id == '1':
        perfil = Perfil('Alison Cassis', 'alison@cassis.com', '11919191911', 'CassisCorp')
    return render(request, 'perfil.html', {'perfil' : perfil})
