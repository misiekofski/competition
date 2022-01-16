from django.contrib import admin

# Register your models here.
from comp2022.models import Exercise, Solution, UserAnswer, Rank, Stage


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'stage', 'exercise_expiration_date', 'points_to_gain')


class StageAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')


class SolutionAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'solution')

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super(SolutionAdmin, self).get_readonly_fields(request, obj)
        if obj:
            return readonly_fields + ('solution', )
        return readonly_fields


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Solution, SolutionAdmin)
admin.site.register(UserAnswer)
admin.site.register(Rank)
admin.site.register(Stage, StageAdmin)


def count_points():
    # this method will count automatically points for provided user solution
    pass
