from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Stage(models.Model):
    # this will allow us to create stages and substages (which will be the same model in DB)
    # https://djangopy.org/how-to/how-to-implement-categories-in-django/
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        # enforcing that there can not be two categories under a parent with same slug
        # __str__ method elaborated later in post.
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "stages"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])


class Exercise(models.Model):
    stage = models.ForeignKey('Stage', on_delete=models.PROTECT, null=True, blank=True)
    title = models.TextField()
    description = models.TextField()
    points_to_gain = models.IntegerField()
    exercise_expiration_date = models.DateTimeField()

    def __str__(self):
        return f"ID: {self.pk}, Tytuł: {self.title}"


class Solution(models.Model):
    exercise = models.OneToOneField('Exercise', on_delete=models.CASCADE)
    solution = models.TextField()


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey('Exercise', on_delete=models.PROTECT)
    solution_provided = models.TextField()
    answer_submitted_at = models.DateTimeField(auto_now=True)
    points_awarded = models.IntegerField(default=0)
    bonus_points = models.IntegerField(default=0)


class Rank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    individual_points_offset = models.IntegerField(default=0)



