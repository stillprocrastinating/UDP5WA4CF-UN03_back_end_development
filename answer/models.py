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
        Question, related_name="question_answers", on_delete=models.CASCADE
    )
    test = models.ForeignKey(
        Test, related_name="test_answers", on_delete=models.CASCADE
    )
    # option = models.IntegerField()
    answer1 = models.IntegerField(default=0)
    answer2 = models.IntegerField(default=0)
    answer3 = models.IntegerField(default=0)
    answer4 = models.IntegerField(default=0)
    answer5 = models.IntegerField(default=0)
    # Create a warning identifier using the highest percentage answer
    # teaching_warning = models.IntegerField(choices=TEACHING_WARNING, default=0)

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
            expected = self.answer1_percentage >= map
            if (expected is True):
                return et
            else:
                return ef

        if (ca == 2):
            expected = self.answer2_percentage >= map
            if (expected is True):
                return et
            else:
                return ef

        if (ca == 3):
            expected = self.answer3_percentage >= map
            if (expected is True):
                return et
            else:
                return ef

        if (ca == 4):
            expected = self.answer4_percentage >= map
            if (expected is True):
                return et
            else:
                return ef

        if (ca == 5):
            expected = self.answer5_percentage >= map
            if (expected is True):
                return et
            else:
                return ef

    @property
    def participant_answer(self):
        if (self.answer1 == 1):
            pa = self.answer1
        elif (self.answer2 == 1):
            pa = self.answer2
        elif (self.answer3 == 1):
            pa = self.answer3
        elif (self.answer4 == 1):
            pa = self.answer4
        elif (self.answer5 == 1):
            pa = self.answer5
        else:
            pa = "No answer"
        return pa
