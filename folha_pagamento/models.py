from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

class Ponto(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data = models.DateField()
    hora_entrada = models.TimeField()
    hora_saida = models.TimeField()




class FolhaPagamento(models.Model):
    mes = models.CharField(max_length=7)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
