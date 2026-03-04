from django.contrib.auth.models import User
from django.db import models
from question.models import Question
from test.models import Test


class Answer(models.Model):
    """
    Stores each answer
    """

    id = models.AutoField(primary_key=True)
    question_id = models.ForeignObject(
        to=Question,
        from_fields=["id"],
        to_fields=[
            "question",
            "sub_answer",
            "sub_answer_number_individual"
            "sub_correct_answer_individual"
        ],
        related_name="question_answers"
    )
    test_id = models.ForeignObject(
        to=Test,
        from_fields=["id"],
        to_fields=["participant_number"],
        related_name="test_answers"
    )
    option = models.IntegerField()
    correct_option_frequency = models.IntegerField()
    incorrect_option_frequency = models.IntegerField()
    tester = models.ForeignKey(User, on_delete=models.SET(str(User.username)))
    # implement warning for individual tester

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.id
