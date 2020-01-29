from django.shortcuts import render
from django.http import HttpResponse

def clientes(request):
    return HttpResponse('Elton, Camila, Elton, Camila,fsdaf')

def cliente_detalhe(request, id):
    return HttpResponse(id)

def cliente_nome(request, nome):
    return HttpResponse('Olá %s' % nome)
