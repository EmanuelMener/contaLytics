from django.db import models

class Processo(models.Model):
    protocolo = models.AutoField(primary_key=True)  # Chave primária automática
    descricao = models.TextField()
    responsavel = models.CharField(max_length=100)
    prazo = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, default='Em andamento')

    def __str__(self):
        return self.descricao
