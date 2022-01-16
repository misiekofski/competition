from django.utils import timezone

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormMixin

from comp2022.forms import UserAnswerForm
from comp2022.models import Exercise


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class ExercisesView(LoginRequiredMixin, ListView):
    model = Exercise
    template_name = 'exercises.html'

    # return only 10 last tasks that are not expired yet
    def get_queryset(self):
        return Exercise.objects.filter(exercise_expiration_date__gte=timezone.now())[:10]


class ExercisesDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = Exercise
    template_name = 'exercise_detail.html'
    form_class = UserAnswerForm

    def get_queryset(self):
        return Exercise.objects.filter(exercise_expiration_date__gte=timezone.now())

