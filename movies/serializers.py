from rest_framework import serializers
from django.db.models import Avg
from .models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()

    def get_average_rating(self, obj):
        average = obj.reviews.aggregate(avg=Avg('rating'))['avg']
        if average is None:
            return None
        return round(float(average), 2)

    def get_reviews_count(self, obj):
        return obj.reviews.count()

    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'description',
            'release_date',
            'genres',
            'average_rating',
            'reviews_count',
            'created_at',
        ]
