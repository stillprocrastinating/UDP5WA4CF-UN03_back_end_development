from django.contrib.auth.models import User
from django.db import models


#LO = (
#    (LO1, "LO1"),
#    (LO2, "LO2"),
#    (LO3, "LO3"),
#    (LO4, "LO4"),
#    (LO5, "LO5"),
#    (LO6, "LO6"),
#    (LO7, "LO7"),
#    (LO8, "LO8"),
#    (LO9, "LO9"),
#    (LO10, "LO10"),
#)

Q_TYPE = (
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

    class LO(models.TextChoices):
        LO1 = "LO1", "LO1 blahblah"
        LO2 = "LO2", "LO2 blahblah"
        LO3 = "LO3", "LO3 blahblah"
        LO4 = "LO4", "LO4 blahblah"
        LO5 = "LO5", "LO5 blahblah"
        LO6 = "LO6", "LO6 blahblah"
        LO7 = "LO7", "LO7 blahblah"
        LO8 = "LO8", "LO8 blahblah"
        LO9 = "LO9", "LO9 blahblah"
        LO10 = "LO10", "LO10 blahblah"

    id = models.CharField(max_length=20, primary_key=True)
    lo = models.CharField(
        choices=LO.choices,
        verbose_name="learning objective"
    )
    type = models.IntegerField(choices=Q_TYPE)
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

    class Meta:
        ordering = ["id"]
        #filtering = ["lo", "type", "author", "warning"]

    def __str__(self):
        return self.id
