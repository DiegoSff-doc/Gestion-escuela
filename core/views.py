from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Sistema de Gestión Escolar - Proyecto Base Listo</h1>")
