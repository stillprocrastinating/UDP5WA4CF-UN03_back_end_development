from django import forms
from .models import Test, Question


class TestNew(forms.ModelForm):
    """
    Generates the form to create Tests
    """
    e1_questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all(),     # fix to have Question.question labels
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Test
        fields = ('id', 'date', 'type', 'participant_number',)
