from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)

    class Meta:
        model = Review
        fields = [
            'id',
            'movie',
            'movie_title',
            'reviewer_name',
            'rating',
            'comment',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at', 'movie_title']
