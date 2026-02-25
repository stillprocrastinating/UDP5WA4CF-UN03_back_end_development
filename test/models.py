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
    (0, "Test"),
    (1, "Resit"),
    (2, "AB")
)


class Test(models.Model):
    """
    Stores each test
    """

    id = models.CharField(max_length=20, primary_key=True)
    slug = AutoSlugField(max_length=20, unique=True, populate_from='id')
    date = models.DateField()
    type = models.IntegerField(choices=T_TYPE)
    participant_number = models.IntegerField(
        verbose_name="number of participants"
    )
    tester = models.ForeignKey(User, on_delete=models.SET(str(User.username)))
    t_difficulty = models.IntegerField(
        choices=T_DIFFICULTY, default=0, verbose_name="test difficulty"
    )
    t_questions = models.ManyToManyField(to=Question)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.id
