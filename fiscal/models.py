from django.db import models

class ResultadoFiscal(models.Model):
    periodo = models.CharField(max_length=7)  # AAAA-MM
    rbt12 = models.DecimalField(max_digits=12, decimal_places=2)
    faturamento_base_mes = models.DecimalField(max_digits=12, decimal_places=2)
    aliquota = models.DecimalField(max_digits=5, decimal_places=2)
    imposto_devido = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Resultado {self.periodo} - R$ {self.imposto_devido}"