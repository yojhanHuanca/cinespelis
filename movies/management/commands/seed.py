from django.core.management.base import BaseCommand  # NUEVO
from movies.models import Genre, Movie  # NUEVO
from datetime import date  # NUEVO


class Command(BaseCommand):  # NUEVO
    help = 'Seed de datos iniciales'  # NUEVO

    def handle(self, *args, **kwargs):  # NUEVO
        self.stdout.write("Seeding data...")

        # 🎭 Géneros
        accion, _ = Genre.objects.get_or_create(name="Acción")
        comedia, _ = Genre.objects.get_or_create(name="Comedia")
        drama, _ = Genre.objects.get_or_create(name="Drama")
        terror, _ = Genre.objects.get_or_create(name="Terror")
        scifi, _ = Genre.objects.get_or_create(name="Ciencia Ficción")

        # 🎬 Películas
        movie1, _ = Movie.objects.get_or_create(
            title="Avengers",
            defaults={
                "description": "Superhéroes salvan el mundo",
                "release_date": date(2012, 5, 4),
            }
        )
        movie1.genres.set([accion, scifi])  # IMPORTANTE

        movie2, _ = Movie.objects.get_or_create(
            title="Titanic",
            defaults={
                "description": "Historia de amor",
                "release_date": date(1997, 12, 19),
            }
        )
        movie2.genres.set([drama])

        movie3, _ = Movie.objects.get_or_create(
            title="It",
            defaults={
                "description": "Payaso aterrador",
                "release_date": date(2017, 9, 8),
            }
        )
        movie3.genres.set([terror])

        movie4, _ = Movie.objects.get_or_create(
            title="The Mask",
            defaults={
                "description": "Comedia con poderes",
                "release_date": date(1994, 7, 29),
            }
        )
        movie4.genres.set([comedia])

        self.stdout.write(self.style.SUCCESS("Seeding completado ✔"))