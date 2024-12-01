from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Processo  # Modelo para processos
from .forms import ProcessoForm  # Formulário (veja o próximo passo)


def dashboard(request):
    processos = Processo.objects.all()  # Busca todos os processos no banco de dados
    return render(request, 'processos/dashboard.html', {'processos': processos})


def criar_processo(request):
    if request.method == 'POST':
        form = ProcessoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('processos:dashboard')  # Redireciona para o dashboard após salvar
    else:
        form = ProcessoForm()

    return render(request, 'processos/criar_processo.html', {'form': form})
