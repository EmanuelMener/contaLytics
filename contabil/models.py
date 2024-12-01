from django.db import models

class Lancamento(models.Model):
    data = models.DateField()
    conta_debito = models.CharField(max_length=255)
    conta_credito = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    historico = models.TextField()

    def __str__(self):
        return f"Lançamento {self.id} - {self.valor}"
