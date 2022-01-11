from django.contrib import admin

# Register your models here.
from comp2022.models import Exercise, Solution, UserAnswer, Rank, Stage

admin.site.register(Exercise)
admin.site.register(Solution)
admin.site.register(UserAnswer)
admin.site.register(Rank)
admin.site.register(Stage)


def count_points():
    # this method will count automatically points for provided user solution
    pass
