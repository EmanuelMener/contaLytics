from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'contabilidade'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Página inicial
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
