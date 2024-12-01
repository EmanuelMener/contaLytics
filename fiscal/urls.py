from django.urls import path
from . import views

app_name = 'fiscal'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('calcular-imposto/', views.calcular_imposto, name='calcular_imposto'),
    path('ver/<int:id>/', views.ver_resultado, name='ver_resultado'),
    path('editar/<int:id>/', views.editar_resultado, name='editar_resultado'),
    path('apagar/<int:id>/', views.apagar_resultado, name='apagar_resultado'),
]
