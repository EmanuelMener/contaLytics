from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contabilidade/', include('contabilidade.urls')),
    path('contabil/', include('contabil.urls')),
    path('fiscal/', include('fiscal.urls')),
    path('folha_pagamento/', include('folha_pagamento.urls')),
    path('processos/', include('processos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # URLs padrão de autenticação
    path('', include('contabilidade.urls')),
]
