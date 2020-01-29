from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return(self.nome)

class Casa(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return(self.nome)

class CPF(models.Model):
    numero = models.CharField(max_length=11, blank=False, null=False)
    data_exp = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.numero

class Cliente(models.Model):
    nome = models.CharField(max_length=70, blank=False, null=False)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()
    cpf = models.OneToOneField(CPF,on_delete=models.CASCADE, blank=True, null=True)
    departamentos = models.ManyToManyField(Departamento, blank=True)

    def __str__(self):
        return self.nome

class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    descricao = models.CharField(max_length=70)
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) #um para muitos

    def __str__(self):
        return self.descricao + ' - ' + self.numero
