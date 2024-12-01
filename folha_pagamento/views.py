from django.shortcuts import render, redirect
from .models import Ponto, Funcionario, FolhaPagamento
from django.contrib import messages
from datetime import datetime
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def dashboard(request):
    funcionarios = Funcionario.objects.all()
    folhas = FolhaPagamento.objects.all()
    return render(request, 'folha_pagamento/dashboard.html', {
        'funcionarios': funcionarios,
        'folhas': folhas,
        'total_funcionarios': funcionarios.count(),
    })
def cadastrar_funcionario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cargo = request.POST.get('cargo')
        salario = request.POST.get('salario')

        # Criação do funcionário
        Funcionario.objects.create(nome=nome, cargo=cargo, salario=salario)

        messages.success(request, 'Funcionário cadastrado com sucesso!')
        return redirect('folha_pagamento:dashboard')  # Ajuste o redirecionamento conforme necessário

    return render(request, 'folha_pagamento/cadastrar_funcionario.html')  # Ajuste o template conforme necessário

def registrar_ponto(request):
    if request.method == 'POST':
        funcionario_id = request.POST.get('funcionario')
        data = request.POST.get('data')
        hora_entrada = request.POST.get('hora_entrada')
        hora_saida = request.POST.get('hora_saida')

        # Valide e registre o ponto
        funcionario = Funcionario.objects.get(id=funcionario_id)
        Ponto.objects.create(
            funcionario=funcionario,
            data=data,
            hora_entrada=hora_entrada,
            hora_saida=hora_saida,
        )

        messages.success(request, 'Ponto registrado com sucesso!')
        return redirect('folha_pagamento:dashboard')

    funcionarios = Funcionario.objects.all()
    return render(request, 'folha_pagamento/registro_ponto.html', {'funcionarios': funcionarios})

def calcular_folha(request):
    """
    Calcula a folha de pagamento para um mês específico.
    Recebe um POST com o formato 'YYYY-MM' para o mês e cria uma entrada de folha de pagamento.
    """
    if request.method == 'POST':
        mes = request.POST.get('mes')  # Formato 'YYYY-MM' vindo do formulário

        if not mes:
            # Caso o campo 'mes' esteja ausente
            return JsonResponse({"erro": "O campo 'mes' é obrigatório."}, status=400)

        try:
            # Adicionar o dia 01 para transformar em um formato válido 'YYYY-MM-DD'
            mes_date = datetime.strptime(f"{mes}-01", "%Y-%m-%d").date()
        except ValueError:
            # Caso o formato do mês seja inválido
            return JsonResponse({"erro": "Formato de mês inválido. Use o formato AAAA-MM."}, status=400)

        try:
            # Criar a folha de pagamento com o mês processado
            folha = FolhaPagamento.objects.create(mes=mes_date)
            return JsonResponse({"mensagem": "Folha de pagamento calculada com sucesso!"}, status=201)
        except Exception as e:
            # Tratar possíveis erros de banco de dados ou outros erros inesperados
            return JsonResponse({"erro": f"Erro ao criar a folha de pagamento: {str(e)}"}, status=500)

    # Caso a requisição não seja POST, redirecionar ou retornar erro
    return JsonResponse({"erro": "Método não permitido. Use POST para esta operação."}, status=405)