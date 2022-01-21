from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from reviews.models import Category, Genre, Title, Comment, Review


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    def validate(self, data):
        title_id = self.context['view'].kwargs.get('title_id')
        user = self.context['request'].user
        if Review.objects.filter(
            user=user,
            title_id=title_id
        ).exists():
            raise serializers.ValidationError("400 Bad Request")
        return data

    class Meta:
        fields = 'id', 'text', 'author', 'score', 'pub_date'
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    def validate(self, data):
        title_id = self.context['view'].kwargs.get('title_id')
        review_id = self.context['view'].kwargs.get('review_id')
        if Review.objects.filter(
            id=review_id,
            title_id=title_id
        ).exists():
            return data
        raise serializers.NotFound()

    class Meta:
        fields = 'id', 'text', 'author', 'pub_date'
        model = Comment
