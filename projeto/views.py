from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    nome = 'Tibuço'
    sexo = 'm'
    
    lista = [
        {'nome': 'Elton', 'sexo': 'm'},
        {'nome': 'Pedro', 'sexo': 'm'},
        {'nome': 'Camila', 'sexo': 'f'},
        {'nome': 'Joana', 'sexo': 'f'},
        {'nome': 'Tiago', 'sexo': 'm'},
    ]
    data = {'nome': nome, 'sexo': sexo, 'lista': lista}
    return render(request, 'index.html', data)
