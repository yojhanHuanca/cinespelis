from django.db.models import Avg, Count
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from movies.models import Movie
from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.select_related('movie').all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        movie_id = self.request.query_params.get('movie')
        if movie_id:
            queryset = queryset.filter(movie_id=movie_id)
        return queryset


class TopMoviesView(APIView):
    def get(self, request):
        top_movies = (
            Movie.objects.annotate(
                average_rating=Avg('reviews__rating'),
                reviews_count=Count('reviews')
            )
            .filter(reviews_count__gt=0)
            .order_by('-average_rating', '-reviews_count', 'title')[:10]
        )

        data = [
            {
                'movie_id': movie.id,
                'title': movie.title,
                'average_rating': round(float(movie.average_rating), 2),
                'reviews_count': movie.reviews_count,
            }
            for movie in top_movies
        ]
        return Response(data)
