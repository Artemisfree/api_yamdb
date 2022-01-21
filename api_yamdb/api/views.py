from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.pagination import PageNumberPagination

from api.serializers import ReviewSerializer, CommentSerializer
from api.permissions import IsOwnerOrModeratorOrAdminOrReadOnly
from reviews.models import Category, Genre, Title, Review
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


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsOwnerOrModeratorOrAdminOrReadOnly]

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        queryset = title.reviews.all()
        return queryset

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        text = self.request.data.get('text')
        score = self.request.data.get('score')
        serializer.save(
            text=text,
            author=self.request.user,
            title=title,
            score=score
        )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsOwnerOrModeratorOrAdminOrReadOnly]

    def get_queryset(self):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        queryset = review.comments.all()
        return queryset

    def perform_create(self, serializer):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        text = self.request.data.get('text')
        serializer.save(
            text=text,
            author=self.request.user,
            review=review
        )
