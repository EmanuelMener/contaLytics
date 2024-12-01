from django.urls import path
from . import views


app_name = 'contabil'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('lancamento/', views.lancamento, name='contabil_lancamento'),
    path('relatorios/', views.relatorios, name='contabil_relatorios'),

    path('novo-lancamento/', views.novo_lancamento, name='novo_lancamento'),
    path('apagar/<int:lancamento_id>/', views.apagar_lancamento, name='apagar_lancamento'),
    path('editar/<int:lancamento_id>/', views.editar_lancamento, name='editar_lancamento'),

]
