from django.db import models

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
    
    class Meta:
        managed = False


class MealView(models.Model):
    mealid = models.IntegerField()
    amount = models.IntegerField()
    unit   = models.IntegerField()
    ingredient_name = models.CharField(max_length=128)
    brand_name = models.CharField(max_length=40)
    category_name = models.CharField(max_length=40)
    serving_size = models.IntegerField()
    serving_unit = models.CharField(max_length=8)
    calories = models.IntegerField()
    fat = models.IntegerField()
    carbohydrates = models.IntegerField()
    protein = models.IntegerField()
    
    class Meta:
        managed = False
