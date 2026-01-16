from django.contrib.auth.models import User
from django.db import models


LO = (
    (0, "Please select learning objective"),
    (1, "LO1"),
    (2, "LO2"),
    (3, "LO3"),
    (4, "LO4"),
    (5, "LO5"),
    (6, "LO6"),
    (7, "LO7"),
    (8, "LO8"),
    (9, "LO9"),
    (10, "LO10"),
)

Q_TYPE = (
    (0, "Please select question type"),
    (1, "Diagram"),
    (2, "Drag & drop"),
    (3, "Multiple choice"),
    (4, "MTC"),     # Match the cards
    (5, "MW"),     # Many word
    (6, "True/false")
)

WARNING = (
    (0, "None"),
    (1, "Warning"),
    (2, "Flag")
)


class Question(models.Model):
    """
    Stores each question
    """

    id = models.CharField(max_length=20, primary_key=True)
    lo = models.IntegerField(
        choices=LO,
        default=0,
        verbose_name="learning objective"
    )
    type = models.IntegerField(choices=Q_TYPE, default=0)
    number = models.IntegerField(verbose_name="number of Qs of that LO & type")
    #question = models.TextField()
    #image = models.ImageField(blank=True)
    sub_number = models.IntegerField(verbose_name="number of subquestions")
    sub_answer_number_individual = models.IntegerField(
        verbose_name="number of answers for subquestion"
    )
    sub_correct_answer_individual = models.IntegerField(
        verbose_name="which answer for subquestion is correct"
    )
    author = models.ForeignKey(User, on_delete=models.SET(str(User.username)))
    warning = models.IntegerField(choices=WARNING, default=0)
