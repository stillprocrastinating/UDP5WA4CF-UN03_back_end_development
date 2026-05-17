# from django.contrib.auth.models import User
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

    ToDo
    Add inputs and outputs (all docstrings)
    """

    question = models.ForeignKey(
        Question, on_delete=models.DO_NOTHING, related_name="question_answers"
    )
    test = models.ForeignKey(
        Test, related_name="test_answers", on_delete=models.CASCADE
    )
    # option = models.IntegerField()
    answer1 = models.IntegerField(default=0,
                                #   name=a1n
                                  )
    answer2 = models.IntegerField(default=0)
    answer3 = models.IntegerField(default=0)
    answer4 = models.IntegerField(default=0)
    answer5 = models.IntegerField(default=0)

    class Meta:
        ordering = ["question"]

    def __str__(self):
        return str(self.id)

    @property
    def correct(self):
        return self.question.sub_correct_answer_individual

    @property
    def participants(self):
        return self.test.participant_number

    @property
    def tester(self):
        return self.test.tester
    
    @property
    def a1n(self):
        return self.question.answer1

    @property
    def answer1_percentage(self):
        a1p = self.answer1 / self.test.participant_number
        return a1p

    @property
    def answer2_percentage(self):
        a2p = self.answer2 / self.test.participant_number
        return a2p

    @property
    def answer3_percentage(self):
        a3p = self.answer3 / self.test.participant_number
        return a3p

    @property
    def answer4_percentage(self):
        a4p = self.answer4 / self.test.participant_number
        return a4p

    @property
    def answer5_percentage(self):
        a5p = self.answer5 / self.test.participant_number
        return a5p

    @property
    def teaching_warning(self):

        ca = self.correct
        map = max(
            self.answer1_percentage,
            self.answer2_percentage,
            self.answer3_percentage,
            self.answer4_percentage,
            self.answer5_percentage
        )

        et = "None."
        ef = "Consider a learning objective teaching method audit."

        if (ca == 1):
            if (self.answer1_percentage >= map):
                return et
            else:
                return ef

        elif (ca == 2):
            if (self.answer2_percentage >= map):
                return et
            else:
                return ef

        elif (ca == 3):
            if (self.answer3_percentage >= map):
                return et
            else:
                return ef

        elif (ca == 4):
            if (self.answer4_percentage >= map):
                return et
            else:
                return ef

        elif (ca == 5):
            if (self.answer5_percentage >= map):
                return et
            else:
                return ef

        else:
            return "Error in calculation. [Answer.teaching_warning]"

    @property
    def participant_answer1(self):
        return str(self.answer1) + " ~~~ " + self.question.answer1

    @property
    def participant_answer2(self):
        return str(self.answer2) + " ~~~ " + self.question.answer2

    @property
    def participant_answer3(self):
        return str(self.answer3) + " ~~~ " + self.question.answer3

    @property
    def participant_answer4(self):
        return str(self.answer4) + " ~~~ " + self.question.answer4

    @property
    def participant_answer5(self):
        return str(self.answer5) + " ~~~ " + self.question.answer5
