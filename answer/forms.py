from django import forms
from .models import Answer, Question, Test


class AnswerNew(forms.ModelForm):
    """
    Generates the form to create Answers
    """
    q_answers = forms.ModelMultipleChoiceField(
        queryset=Question.objects.filter(Test.t_questions),     # fix to have Question.answerx labels
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Answer
        fields = ('question_id', 'test_id', 'option', 'correct_option_frequency', 'incorrect_option_frequency')

    def __str__(self):
        return Answer.correct_option_frequency
