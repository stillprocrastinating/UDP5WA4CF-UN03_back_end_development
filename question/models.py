from django.contrib.auth.models import User
from django.db import models
from .models import Objective


Q_TYPE = (
    (1, "Diagram"),
    (2, "Drag & drop"),
    (3, "Multiple choice"),
    (4, "Matching"),
    (5, "Missing word"),
    (6, "True/false")
)

Q_DIFFICULTY = (
    (0, "Error in calculation"),
    (1, "Easy"),
    (2, "Optimal"),
    (3, "Difficult")
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
    slug = models.SlugField(max_length=20, unique=True)
    lo = models.ForeignKey(Objective, related_name="objective_question")
    type = models.IntegerField(choices=Q_TYPE)
    number = models.IntegerField(verbose_name="number of Qs of that LO & type")
    #question = models.TextField()     # extend.ucl.ac.uk
    #image = models.ImageField(blank=True)
    sub_number = models.IntegerField(verbose_name="number of subquestions")
    sub_answer_number_individual = models.IntegerField(
        verbose_name="number of answers for subquestion"
    )
    sub_correct_answer_individual = models.IntegerField(
        verbose_name="which answer for subquestion is correct"
    )
    author = models.ForeignKey(User, on_delete=models.SET(str(User.username)))
    q_difficulty = models.IntegerField(
        choices=Q_DIFFICULTY, default=0, verbose_name="question difficulty"
    )
    warning = models.IntegerField(choices=WARNING, default=0)

    class Meta:
        ordering = ["id"]
        #filtering = ["lo", "type", "author", "warning"]

    def __str__(self):
        return self.id
