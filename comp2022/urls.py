from django.urls import path

from comp2022.views import HomeView, ExercisesView, ExercisesDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('zadania/', ExercisesView.as_view(), name='exercises'),
    path('zadania/<int:pk>', ExercisesDetailView.as_view(), name='exercise-detail'),
]
