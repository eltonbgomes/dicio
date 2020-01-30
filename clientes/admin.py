from django.contrib import admin
from .models import Cliente, Telefone, CPF, Departamento

class Clienteadmin(admin.ModelAdmin):
    fields = ('nome', 'endereco', 'salario', 'idade', 'cpf', 'departamentos')
    list_display = ('id', 'nome', 'endereco', 'email')
    list_filter = ('departamentos',)
    search_fields = ('id', 'nome', 'email', 'departamentos__nome')



admin.site.register(Cliente, Clienteadmin)
admin.site.register(Telefone)
admin.site.register(CPF)
admin.site.register(Departamento)