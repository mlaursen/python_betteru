from django.db import models
from django.db.models import Manager, Model

from accounts.models import Account
from meals.models import Meal
from django.utils import timezone
# Create your models here.



class Goal(Model):
    """
    So what is in a goal.

    date
    account
    expected_calories
    expected_fat
    expected_carbohydrates
    expected_protein

    goalpart
    date
    account
    meal
    """
    date = models.DateTimeField()
    account = models.ForeignKey(Account)
    expected_calories = models.DecimalField(max_digits=8, decimal_places=2)
    expected_fat = models.DecimalField(max_digits=8, decimal_places=2)
    expected_carbohydrates = models.DecimalField(max_digits=8, decimal_places=2)
    expected_protein = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        s  = "id: %s\n" % self.id
        s += "date: %s\n" % self.date
        return s


class GoalPart(Model):
    goal = models.ForeignKey(Goal)
    meal = models.ForeignKey(Meal)

    def __str__(self):
        s  = "id: %s\n" % self.id
        s += "goal: %s\n" % str(self.goal)
        s += "meal: %s\n" % str(self.meal)
        return s

