from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('tarefa-lista/', views.tarefa_lista, name='tarefa-lista'),
    path('tarefa-detalhes/<str:pk>', views.tarefa_detalhes, name='tarefa-detalhes'),
    path('tarefa-criar/', views.tarefa_criar, name='tarefa-criar'),
    path('tarefa-atualizar/<str:pk>', views.tarefa_atualizar, name='tarefa-atualizar'),
    path('tarefa-deletar/<str:pk>', views.tarefa_deletar, name='tarefa-deletar')
]
