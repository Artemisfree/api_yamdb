from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .models import User


class AdminViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # пока не знаю, что писать
    # serializer_class = ?
    # permission_class = ?
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('username',)
