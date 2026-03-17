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
    question_id = models.ForeignKey(Question, related_name="question_answers", on_delete=models.SET(str(Question.question)))
    test_id = models.ForeignKey(Test, related_name="test_answers", on_delete=models.SET(str(Test.id)))
    participants = Test.participant_number
    # option = models.IntegerField()
    answer1 = models.IntegerField(default=0)
    answer2 = models.IntegerField(default=0)
    answer3 = models.IntegerField(default=0)
    answer4 = models.IntegerField(default=0)
    answer5 = models.IntegerField(default=0)
    # answer1_percentage = models.Expression(answer1 / participants)
    # answer2_percentage = models.Expression(answer2 / participants)
    # answer3_percentage = models.Expression(answer3 / participants)
    # answer4_percentage = models.Expression(answer4 / participants)
    # answer5_percentage = models.Expression(answer5 / participants)
    correct = Question.sub_correct_answer_individual
    # # Create a warning identifier using the highest percentage answer
    tester = models.ForeignKey(User, on_delete=models.SET(str(User.username)))
    teaching_warning = models.IntegerField(choices=TEACHING_WARNING, default=0)

    class Meta:
        ordering = ["question_id"]

    def __str__(self):
        return self.id
