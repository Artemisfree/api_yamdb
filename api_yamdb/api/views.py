from rest_framework import filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from reviews.models import Category, Genre, Title
from .permissions import AdminOrReadOnly
from .serializers import (CategorySerializer, GenreSerializer, TitleSerializer)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AdminOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['name', ]


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AdminOrReadOnly]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['name', ]


class TitleViewSet(viewsets.ModelViewSet):
    permission_classes = [AdminOrReadOnly]
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend,)
    pagination_class = None
    filterset_fields = ('category', 'genre', 'name', 'year')
