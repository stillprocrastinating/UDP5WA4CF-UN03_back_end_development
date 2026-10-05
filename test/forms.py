from django import forms
from .models import Question, Test


class TestNew(forms.ModelForm):
    """
    Generates the form to create Tests
    """
    e1_questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Test
        fields = ('id', 'date', 'type', 'participant_number',)

    def __str__(self):
        return Question.question
