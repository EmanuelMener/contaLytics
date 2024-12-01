from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import ResultadoFiscal  # Model para salvar resultados
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from .models import ResultadoFiscal
from django.views.decorators.csrf import csrf_exempt

def dashboard(request):
    resultados = ResultadoFiscal.objects.all()
    total_impostos = sum(resultado.imposto_devido for resultado in resultados)
    return render(request, 'fiscal/dashboard.html', {
        'resultados': resultados,
        'total_impostos': total_impostos
    })
def calcular_imposto(request):
    if request.method == "POST":
        rbt12 = float(request.POST.get("rbt12"))
        faturamento_base_mes = float(request.POST.get("faturamento_base_mes"))
        periodo = request.POST.get("periodo")

        # Lógica de cálculo da alíquota e imposto devido (simples exemplo)
        if rbt12 <= 180000:  # Faixa do Simples Nacional
            aliquota = 6.0  # Alíquota fixa para esta faixa
        elif rbt12 <= 360000:
            aliquota = 11.2
        else:
            aliquota = 13.5

        imposto_devido = faturamento_base_mes * (aliquota / 100)

        # Salvar no banco
        resultado = ResultadoFiscal.objects.create(
            periodo=periodo,
            rbt12=rbt12,
            faturamento_base_mes=faturamento_base_mes,
            aliquota=aliquota,
            imposto_devido=imposto_devido,
        )

        return redirect("fiscal:dashboard")  # Redireciona para o dashboard

    # Renderiza o formulário de cálculo
    return render(request, "fiscal/dashboard.html")


# Dashboard
# Ver
def ver_resultado(request, id):
    resultado = get_object_or_404(ResultadoFiscal, id=id)
    data = {
        'periodo': resultado.periodo,
        'rbt12': str(resultado.rbt12),
        'faturamento_base_mes': str(resultado.faturamento_base_mes),
        'aliquota': str(resultado.aliquota),
        'imposto_devido': str(resultado.imposto_devido),
    }
    return JsonResponse(data)

# Editar
@csrf_exempt
def editar_resultado(request, id):
    resultado = get_object_or_404(ResultadoFiscal, id=id)

    if request.method == 'POST':
        # Atualizar os campos recebidos do formulário
        resultado.periodo = request.POST.get('periodo')
        resultado.rbt12 = request.POST.get('rbt12')
        resultado.faturamento_base_mes = request.POST.get('faturamento_base_mes')
        resultado.aliquota = request.POST.get('aliquota')

        # Calcular o imposto devido, se necessário
        resultado.imposto_devido = (
                float(resultado.faturamento_base_mes) * (float(resultado.aliquota) / 100)
        )

        # Salvar o resultado atualizado
        resultado.save()
        return redirect("fiscal:dashboard")  # Redireciona para o dashboard

    # Retornar os dados para a edição
    return JsonResponse({
        'periodo': resultado.periodo,
        'rbt12': str(resultado.rbt12),
        'faturamento_base_mes': str(resultado.faturamento_base_mes),
        'aliquota': str(resultado.aliquota),
        'imposto_devido': str(resultado.imposto_devido),
    })

# Apagar
@csrf_exempt
def apagar_resultado(request, id):
    resultado = get_object_or_404(ResultadoFiscal, id=id)
    if request.method == 'DELETE':
        resultado.delete()
        return redirect("fiscal:dashboard")  # Redireciona para o dashboard
    return JsonResponse({'error': 'Método não permitido'}, status=405)

