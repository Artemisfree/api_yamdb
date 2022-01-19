from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination

from api.serializers import ReviewSerializer, CommentSerializer

from reviews.models import Review, Title
from api.permissions import IsOwnreOrModeratorOrAdminOrReadOnly


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsOwnreOrModeratorOrAdminOrReadOnly]

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
    permission_classes = [IsOwnreOrModeratorOrAdminOrReadOnly]

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        # review_id = self.kwargs.get('review_id')
        title = get_object_or_404(Title, id=title_id)
        # Нужно еще подумать
        # review = get_object_or_404(Review, id=review_id)
        queryset = title.reviews.comments.all()
        return queryset

    def perform_create(self, serializer):
        # title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        # title = get_object_or_404(Title, id=title_id)
        review = get_object_or_404(Review, id=review_id)
        text = self.request.data.get('text')
        serializer.save(
            text=text,
            author=self.request.user,
            review=review
        )
