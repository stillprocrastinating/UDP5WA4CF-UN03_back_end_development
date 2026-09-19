from django import forms
from .models import Answer


class AnswerNew(forms.ModelForm):
    """
    Generates the form to create Answers
    """

    class Meta:
        model = Answer
        fields = (
            'test',
            'question',
            'answer1', 'answer2', 'answer3', 'answer4', 'answer5',
        )
