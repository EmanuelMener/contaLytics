from django.shortcuts import render, redirect
from .models import Lancamento
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def dashboard(request):
    lancamentos_recentes = Lancamento.objects.all()[:10]
    return render(request, 'contabil/dashboard.html', {'lancamentos': lancamentos_recentes})

def lancamento(request):
    # Calcular o próximo ID
    ultimo_lancamento = Lancamento.objects.order_by('-id').first()
    proximo_id = (ultimo_lancamento.id + 1) if ultimo_lancamento else 1

    return render(request, 'contabil/lancamento.html', {'proximo_id': proximo_id})

def relatorios(request):
    return render(request, 'contabil/relatorios.html')  # Template para relatórios

def novo_lancamento(request):
    if request.method == 'POST':
        # Recebe os dados do formulário
        data = request.POST.get('data')
        conta_debito = request.POST.get('conta_debito')
        conta_credito = request.POST.get('conta_credito')
        valor = request.POST.get('valor')
        historico = request.POST.get('historico')

        # Salva no banco de dados (ID gerado automaticamente)
        Lancamento.objects.create(
            data=data,
            conta_debito=conta_debito,
            conta_credito=conta_credito,
            valor=valor,
            historico=historico,
        )
        return redirect('contabil:dashboard')  # Redireciona para o dashboard

    return render(request, 'contabil/dashboard.html')

def apagar_lancamento(request, lancamento_id):
    if request.method == "DELETE":
        lancamento = get_object_or_404(Lancamento, id=lancamento_id)
        lancamento.delete()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False}, status=400)

def editar_lancamento(request, lancamento_id):
    lancamento = get_object_or_404(Lancamento, id=lancamento_id)

    if request.method == "GET":
        return JsonResponse({
            "data": lancamento.data.strftime('%Y-%m-%d'),
            "conta_debito": lancamento.conta_debito,
            "conta_credito": lancamento.conta_credito,
            "valor": lancamento.valor,
            "historico": lancamento.historico,
        })

    elif request.method == "POST":
        lancamento.data = request.POST.get("data")
        lancamento.conta_debito = request.POST.get("conta_debito")
        lancamento.conta_credito = request.POST.get("conta_credito")
        lancamento.valor = request.POST.get("valor")
        lancamento.historico = request.POST.get("historico")
        lancamento.save()

        return redirect("contabil:dashboard")
