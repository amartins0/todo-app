# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Tarefa


# API Overview
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Lista': '/tarefa-lista/',
        'Detalhes View': '/tarefa-detalhes/<str:pk>/',
        'Criar': '/tarefa-criar/',
        'atualizar': '/tarefa-atualizar/<str:pk>/',
        'Deletar': '/tarefa-deletar/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def tarefa_lista(request):
    tarefa = Tarefa.objects.all()
    serializer = TaskSerializer(tarefa, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def tarefa_detalhes(request, pk):
    tarefa = Tarefa.objects.get(id=pk)
    serializer = TaskSerializer(tarefa, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def tarefa_criar(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def tarefa_atualizar(request, pk):
    task = Tarefa.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def tarefa_deletar(request, pk):
    tarefa = Tarefa.objects.get(id=pk)

    tarefa.delete()
    return Response("Tarefa deletada!")
