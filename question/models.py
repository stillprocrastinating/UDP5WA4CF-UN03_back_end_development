from autoslug import AutoSlugField
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
    (11, "LO11 To explain the Five Freedoms and how these apply to laboratory species."),
    (12, "LO12 To describe the concept of harms to animals including avoidable and unavoidable suffering, direct, contingent, and cumulative suffering."),
    (13, "LO13 To describe the importance of good animal welfare including its' effect on scientific outcomes as well as for societal and moral reasons."),
    (14, "LO14 To describe the responsibility of humans when working with research animals and recognise the importance of having a respectful and humane attitude towards working with animals in research."),
)

Q_CORRECT = (
    (1, "Answer1"),
    (2, "Answer2"),
    (3, "Answer3"),
    (4, "Answer4"),
    (5, "Answer5")
)

Q_DIFFICULTY = (
    (0, "Error in calculation"),
    (1, "Easy"),
    (2, "Optimal"),
    (3, "Difficult")
)

Q_TYPE = (
    (1, "Diagram"),
    (2, "Drag & drop"),
    (3, "Multiple choice"),
    (4, "Matching"),
    (5, "Missing word"),
    (6, "True/false")
)

WARNING = (
    (0, "Error in calculation"),
    (1, "None"),
    (2, "Warning"),
    (3, "Flagged to revise question wording")
)


class Question(models.Model):
    """
    Stores each question
    """

    id = models.CharField(max_length=25, primary_key=True)
    slug = AutoSlugField(max_length=25, unique=True, populate_from='id')
    lo = models.IntegerField(
        choices=LO,
        verbose_name="learning objective"
    )
    type = models.IntegerField(choices=Q_TYPE)
    number = models.IntegerField(verbose_name="number of Qs of that LO & type")
    question = models.TextField()     # extend.ucl.ac.uk
    answer1 = models.TextField()     # extend.ucl.ac.uk
    answer2 = models.TextField()     # extend.ucl.ac.uk
    answer3 = models.TextField(blank=True)     # extend.ucl.ac.uk
    answer4 = models.TextField(blank=True)     # extend.ucl.ac.uk
    answer5 = models.TextField(blank=True)     # extend.ucl.ac.uk
    #image = models.ImageField(blank=True)     # not needed for this iteration of the app
    sub_number = models.IntegerField(verbose_name="number of subquestions")
    sub_answer_number_individual = models.IntegerField(
        verbose_name="number of answers for subquestion"
    )
    sub_correct_answer_individual = models.IntegerField(
        choices=Q_CORRECT,
        verbose_name="which answer for subquestion is correct"
    )
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    q_difficulty = models.IntegerField(
        choices=Q_DIFFICULTY, default=0, verbose_name="question difficulty"
    )
    warning = models.IntegerField(choices=WARNING, default=0)

    class Meta:
        ordering = ["lo", "type", "number"]
        #filtering = ["lo", "type", "author", "warning"]

    def __str__(self):
        return self.question
