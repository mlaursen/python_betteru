from django.db import models
from utils.util import in_ttuple
from ingredients.models import Ingredient

class MealPartManager(models.Manager):
    def create_mealpart(self, mealid, ingredientid, amount, unit):
        if not Meal.objects.filter(id=mealid) or not Ingredient.objects.filter(id=ingredientid) or not in_ttuple(MealPart.UNITS, unit):
            return False
        else:
            i = Ingredient.objects.get(id=ingredientid)
            return self.create(mealid=mealid, ingredient=i, amount=amount, unit=unit)


class MealPart(models.Model):
    UNITS = (
        (0, 'Default'),
        (1, 'Alternate'),
    )
    mealid = models.IntegerField()
    ingredient = models.ForeignKey(Ingredient)
    amount = models.IntegerField(default=0)
    unit = models.IntegerField(max_length=1, choices=UNITS)

    objects = MealPartManager()

    def __str__(self):
        s = "id: " + str(self.id)
        s += ", mealid: " + str(self.mealid)
        s += ", ingredient: " + str(self.ingredient)
        s += ", amt: " + str(self.amount)
        s += ", unit: " + str(self.unit)
        return s
    
class MealManager(models.Manager):

    def create_meal(self, name, description):
        m = self.create(name=name,
                description=description
                )
        return m



class Meal(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    objects = MealManager()

    def __str__(self):
        s  = "id: %s\nname: %s\ndescription: %s\nparts: (\n" % (self.id, self.name, self.description)
        parts = MealPart.objects.filter(mealid=self.id)
        for p in parts:
            s += "\t(%s),\n" % str(p)
        s += ")\n"
        return s

class MealPartsView(models.Model):
    mealid = models.IntegerField()
    amount = models.IntegerField()
    unit   = models.IntegerField()
    ingredient_name = models.CharField(max_length=128)
    brand_name = models.CharField(max_length=40)
    category_name = models.CharField(max_length=40)
    default_serving_size = models.IntegerField()
    default_serving_unit = models.CharField(max_length=8)
    alt_serving_size = models.IntegerField()
    alt_serving_unit = models.CharField(max_length=8)
    calories = models.IntegerField()
    fat = models.IntegerField()
    carbohydrates = models.IntegerField()
    protein = models.IntegerField()
    total_calories = models.IntegerField()
    total_fat = models.IntegerField()
    total_carbohydrates = models.IntegerField()
    total_protein = models.IntegerField()
    serving_size = models.IntegerField()
    serving_unit = models.CharField(max_length=8)
    
    class Meta:
        managed = False
        db_table = 'MEALPARTS_VIEW'


class MealView(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    total_calories = models.DecimalField(max_digits=8, decimal_places=2)
    total_fat = models.DecimalField(max_digits=8, decimal_places=2)
    total_carbohydrates = models.DecimalField(max_digits=8, decimal_places=2)
    total_protein = models.DecimalField(max_digits=8, decimal_places=2)
    
    class Meta:
        managed = False
        db_table = 'MEAL_VIEW'




def create_full_meal(name, description, meal_parts):
    """
    Creates a 'full' meal.
    Creates a meal with name and description and then creates
    each and every mealpart to that associated meal
    Useage:
    create_full_meal('Example', 'Example desc', [[2, 300, 1], [1, 2, 0]])
    """
    INGREDIENT_ID = 0
    AMOUNT = 1
    UNIT = 2

    m = Meal.objects.create_meal(name, description)
    mid = m.id
    mps = []
    for meal_part in meal_parts:
        mp = MealPart.objects.create_mealpart(mid,
                meal_part[INGREDIENT_ID],
                meal_part[AMOUNT],
                meal_part[UNIT]
        )
        mps.append(mp)

    return [m, mps]










