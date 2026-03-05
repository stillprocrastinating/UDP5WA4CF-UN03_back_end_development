from django.contrib.auth.models import User
from django.db import models
from question.models import Question
from test.models import Test


TEACHING_WARNING = (
    (0, "Error in calculation"),
    (1, "None"),
    (2, "Warning"),
    (3, "Flagged to revise teaching method")
)


class Answer(models.Model):
    """
    Stores each answer
    """

    id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(
        to=Question,
        related_name="question_answers",
        on_delete=models.SET(str(Question.question))
    )
    test_id = models.ForeignKey(
        to=Test,
        related_name="test_answers",
        on_delete=models.SET(str(Test.id))
    )
    # option = models.IntegerField()
    correct_option_frequency = models.IntegerField()
    incorrect_option_frequency = models.IntegerField()
    tester = models.ForeignKey(User, on_delete=models.SET(str(User.username)))
    teaching_warning = models.IntegerField(choices=TEACHING_WARNING, default=0)

    class Meta:
        ordering = ["question_id"]

    def __str__(self):
        return self.id
