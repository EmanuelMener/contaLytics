from django.urls import path
from . import views

app_name = 'processos'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('criar/', views.criar_processo, name='criar_processo'),  # Adicionando a URL 'criar_processo'
    # Outras URLs do módulo processos
]
