from django import forms
from .models import Answer


class AnswerNew(forms.ModelForm):
    """
    Generates the form to create Answers
    """
    # q_answers = forms.ModelMultipleChoiceField(
    #     queryset=Question.objects.filter(Test.t_questions),     # fix to have Question.answerx labels
    #     widget=forms.CheckboxSelectMultiple
    # )

    class Meta:
        model = Answer
        # fields = ('question_id', 'test_id', 'option', 'correct_option_frequency', 'incorrect_option_frequency')
        fields = ('test', 'question', 'answer1', 'answer2', 'answer3','answer4', 'answer5',)
