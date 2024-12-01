from django.urls import path
from . import views

app_name = 'folha_pagamento'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cadastrar-funcionario/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('registrar-ponto/', views.registrar_ponto, name='registrar_ponto'),
    path('calcular-folha/', views.calcular_folha, name='calcular_folha'),
]
