from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

from .models import *
from .serializers import *


class GameViewSet(viewsets.ViewSet):
  """Вывод списка игр"""

  permission_classes = [permissions.IsAuthenticated]

  def list(self, request):
    queryset = Game.objects.all()
    serializer = GameListSerializer(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self, request, pk):
    queryset = Game.objects.all()
    game = get_object_or_404(queryset, pk=pk)
    serializer = GameDetailSerializer(game)
    return Response(serializer.data)


class DeveloperViewSet(viewsets.ViewSet):
  """Вывод списка разработчиков и издателей"""

  def list(self, request):
    queryset = Developer.objects.all()
    serializer = DeveloperListSerializer(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self, request, pk):
    queryset = Developer.objects.all()
    developer = get_object_or_404(queryset, pk=pk)
    serializer = DeveloperDetailSerializer(developer)
    return Response(serializer.data)


class ReviewCreateViewSet(viewsets.ModelViewSet):
  """Добавление отзыва к игре"""

  serializer_class = ReviewCreateSerializer
