import random
from datetime import date
from django.core.management.base import BaseCommand
from movies.models import Genre, Movie
from reviews.models import Review


class Command(BaseCommand):
    help = 'Carga datos de prueba para genres, movies y reviews.'

    def add_arguments(self, parser):
        parser.add_argument('--movies', type=int, default=15, help='Cantidad de peliculas a crear')
        parser.add_argument('--reviews', type=int, default=45, help='Cantidad de reviews a crear')

    def handle(self, *args, **options):
        movies_count = options['movies']
        reviews_count = options['reviews']

        genre_names = [
            'Accion', 'Comedia', 'Drama', 'Ciencia Ficcion', 'Terror',
            'Aventura', 'Romance', 'Animacion', 'Suspenso', 'Fantasia',
        ]
        reviewer_names = [
            'Ana', 'Luis', 'Camila', 'Diego', 'Valeria',
            'Marco', 'Lucia', 'Pedro', 'Sofia', 'Andres',
        ]
        descriptions = [
            'Una historia emocionante con giros inesperados.',
            'Una pelicula ideal para ver en familia.',
            'Un relato intenso con gran desarrollo de personajes.',
            'Una propuesta visual atractiva y entretenida.',
            'Una narrativa dinamica con momentos memorables.',
        ]

        genres = [Genre.objects.get_or_create(name=name)[0] for name in genre_names]

        created_movies = []
        next_index = Movie.objects.count() + 1
        for i in range(movies_count):
            movie = Movie.objects.create(
                title=f'Pelicula Demo {next_index + i}',
                description=random.choice(descriptions),
                release_date=date(
                    random.randint(1995, 2025),
                    random.randint(1, 12),
                    random.randint(1, 28),
                ),
            )
            movie.genres.set(random.sample(genres, k=random.randint(1, 3)))
            created_movies.append(movie)

        all_movies = list(Movie.objects.all())
        created_reviews = 0
        for _ in range(reviews_count):
            movie = random.choice(all_movies)
            Review.objects.create(
                movie=movie,
                reviewer_name=random.choice(reviewer_names),
                rating=random.randint(1, 5),
                comment=random.choice(descriptions),
            )
            created_reviews += 1

        self.stdout.write(self.style.SUCCESS(f'Generos totales: {Genre.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Peliculas creadas: {len(created_movies)}'))
        self.stdout.write(self.style.SUCCESS(f'Reviews creadas: {created_reviews}'))
