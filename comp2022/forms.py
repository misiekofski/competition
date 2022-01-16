from django import forms

from comp2022.models import UserAnswer


class UserAnswerForm(forms.ModelForm):
    class Meta:
        model = UserAnswer
        fields = ['solution_provided']
