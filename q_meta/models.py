from django.db import models
from question.models import Question
from answer.models import Answer


class Q_meta(models.Model):
    """
    Stores each :model:`question.Question` meta data
    """

    question = models.ForeignKey(
        Question, on_delete=models.DO_NOTHING, related_name="question_analyses"
    )
    answer = models.ForeignKey(
        Answer, on_delete=models.CASCADE, related_name="q_meta_answers"
    )

    def __str__(self):
        return str(self.id)

    @property
    def warning(self):
        # return str(sum(self.answer.teaching_warning))
        return "Test"
