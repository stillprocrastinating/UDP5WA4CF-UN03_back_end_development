from django.contrib.auth.models import User
from django.db import models


T_TYPE = (
    (0, "Test"),
    (1, "Resit"),
    (2, "AB")
)

T_DIFFICULTY = (
    (0, "Error in calculation"),
    (1, "Easy"),
    (2, "Optimal"),
    (3, "Difficult")
)


class Test(models.Model):
    """
    Stores each test
    """

    id = models.CharField(max_length=20, primary_key=True)
    slug = models.SlugField(max_length=20, unique=True)
    date = models.DateTimeField()
    type = models.IntegerField(choices=T_TYPE)
    participant_number = models.IntegerField()
    tester = models.ForeignKey(User, on_delete=models.SET(str(User.username)))
    t_difficulty = models.IntegerField(
        choices=T_DIFFICULTY, default=0, verbose_name="test difficulty"
    )

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.id
