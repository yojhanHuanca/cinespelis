from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, TopMoviesView

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet)

urlpatterns = router.urls + [
    path('top-movies/', TopMoviesView.as_view(), name='top-movies'),
]
