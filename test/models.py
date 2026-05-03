from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models
from question.models import Question


T_DIFFICULTY = (
    (0, "Error in calculation"),
    (1, "Easy"),
    (2, "Optimal"),
    (3, "Difficult")
)

T_TYPE = (
    (0, "E1/L PiLAB Test"),
    (1, "PiLAB Test"),
    (2, "Resit")
)


class Test(models.Model):
    """
    Stores each test
    """

    id = models.CharField(max_length=25, primary_key=True)
    slug = AutoSlugField(max_length=25, unique=True, populate_from='id')
    date = models.DateField()
    type = models.IntegerField(choices=T_TYPE)
    participant_number = models.IntegerField(
        verbose_name="number of participants"
    )
    tester = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    t_difficulty = models.IntegerField(
        choices=T_DIFFICULTY, default=0, verbose_name="test difficulty"
    )
    t_questions = models.ManyToManyField(to=Question)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.id
