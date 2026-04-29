from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=120)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.movie.title} - {self.rating}/5 by {self.reviewer_name}"
