from django import forms
from .models import Test


class TestNew(forms.ModelForm):
    """
    Generates the form to create Tests
    """

    class Meta:
        model = Test
        fields = ('id', 'date', 'type', 'participant_number',)
