from django.contrib import admin
from .models import Movie, Genre  # CAMBIO

# NUEVO
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # IMPORTANTE


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date')
    filter_horizontal = ('genres', 'actors')  # IMPORTANTE (mejor UI)