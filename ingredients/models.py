from django.db import models



class BrandManager(models.Manager):
    def create_brand(self, name):
        return self.create(name=name)

class Brand(models.Model):
    name = models.CharField(max_length=40)

    objects = BrandManager()

    def __str__(self):
        return self.name


class CategoryManager(models.Manager):
    def create_category(self, name):
        return self.create(name=name)

class Category(models.Model):
    name = models.CharField(max_length=40)

    objects = CategoryManager()

    def __str__(self):
        return self.name





class IngredientManager(models.Manager):
    def create_ingredient(self, name, brand, catg, dservingsize, dservingunit, aservingsize, aservingunit, cal, fat, carb, prot):
        brand = Brand.objects.get(name=brand)
        catg  = Category.objects.get(name=catg)
        ingredient = self.create(name=name,
                brand=brand,
                category=catg,
                default_serving_size=dservingsize,
                default_serving_unit=dservingunit,
                alt_serving_size=aservingsize,
                alt_serving_unit=aservingunit,
                calories=cal,
                fat=fat,
                carbohydrates=carb,
                protein=prot
        )
        return ingredient


class Ingredient(models.Model):
    name = models.CharField(max_length=128)
    brand = models.ForeignKey(Brand)
    category = models.ForeignKey(Category)
    default_serving_size = models.IntegerField(default=0)
    default_serving_unit = models.CharField(max_length=15)
    alt_serving_size = models.IntegerField(default=0)
    alt_serving_unit = models.CharField(max_length=15)
    calories = models.IntegerField()
    fat = models.IntegerField()
    carbohydrates = models.IntegerField()
    protein = models.IntegerField()

    objects = IngredientManager()

    def __str__(self):
        return self.name

