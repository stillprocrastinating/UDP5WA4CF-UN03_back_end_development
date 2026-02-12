from django.contrib.auth.models import User
from django.db import models


LO = (
    (1, "LO1 To understand the historical framework of ASPA and the ethics behind it."),
    (2, "LO2 To state what the ethical framework which underpins ASPA is and how programs of work are justified, by weighing likely adverse effects on the animals against the likely benefits."),
    (3, "LO3 To define the 3Rs. Indicate what they are for and how these relate to ethical principles."),
    (4, "LO4 To identify relevant sources of information relating to ethics and the 3Rs."),
    (5, "LO5 To identify ethical and animal welfare issues in their own work."),
    (6, "LO6 To explain the limits of what is considered permissible to do within a research establishment and how cultural, national, temporal, and institutional factors can differ."),
    (7, "LO7 To discuss to what extent welfare issues, pain, suffering, distress, and lasting harm should be interpreted."),
    (8, "LO8 To explain what a culture of care is, its importance, and how they may contribute."),
    (9, "LO9 To recognise the importance of ethical responsibility and identify the consequences of their actions—connected to culture of care."),
    (10, "LO10 To explain the purpose of the local AWERB."),
)

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
    (0, "Error in calculation"),
    (1, "None"),
    (2, "Warning"),
    (3, "Flag")
)


class Question(models.Model):
    """
    Stores each question
    """

    id = models.CharField(max_length=20, primary_key=True)
    slug = models.SlugField(max_length=20, unique=True)
    lo = models.IntegerField(
        choices=LO,
        verbose_name="learning objective"
    )
    type = models.IntegerField(choices=Q_TYPE)
    number = models.IntegerField(verbose_name="number of Qs of that LO & type")
    question = models.TextField()     # extend.ucl.ac.uk
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
