from django.db import models


class RegUser(models.Model):
    name = models.CharField(max_length=100, blank=False)
    branch = models.CharField(max_length=50, blank=False)
    CHOICES = [('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth'),
               ('5', 'Fifth'), ('6', 'Sixth'), ('7', 'Seventh'), ('8', 'Eighth')]
    semester = models.CharField(
        choices=CHOICES, max_length=20, blank=False
    )
    course = models.CharField(max_length=100, blank=False)
    gender_choice = [('1', 'Male'), ('2', 'Female'), ('3', 'Other'), ('4', 'Preferred Not to Say')]
    gender = models.CharField(choices=gender_choice, max_length=20, blank=False)
    email = models.EmailField(max_length=150, blank=False)
    WNumber = models.CharField(max_length=10, blank=False)
