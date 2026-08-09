from django import forms
from .models import Answer


class AnswerNewTest(forms.ModelForm):
    """
    Generates the form to create Answers by selecting the Test
    """

    class Meta:
        model = Answer
        fields = ('test',)


class AnswerNewQuestion(forms.ModelForm):
    """
    Generates the form to create Answers by selecting the Question

    Relies on :form:`AnswerNewTest`
    """

    class Meta:
        model = Answer
        fields = ('question',)


class AnswerNewAnswers(forms.ModelForm):
    """
    Generates the form to create Answers by selecting the Answers

    Relies on :form:`AnswerNewQuestion`
    """

    class Meta:
        model = Answer
        fields = ('answer1', 'answer2', 'answer3', 'answer4', 'answer5',)
