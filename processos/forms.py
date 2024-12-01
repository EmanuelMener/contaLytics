from django import forms
from .models import Processo

class ProcessoForm(forms.ModelForm):
    class Meta:
        model = Processo
        fields = ['descricao', 'responsavel', 'prazo']  # Campos do modelo Processo
