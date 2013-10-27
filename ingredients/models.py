from django.db import models



class BrandManager(models.Manager):
    def ceate_brand(self, name):
        return self.create(name=name)

class Brand(models.Model):
    name = models.CharField(max_length=40)

    objects = BrandManager()

    def __str__(self):
        return self.name


class CategoryManager(models.Manager):
    def create_brand(self, name):
        return self.create(name=name)

class Category(models.Model):
    name = models.CharField(max_length=40)

    objects = CategoryManager()

    def __str__(self):
        return self.name





class IngredientManager(models.Manager):
    def create_ingredient(self, brand, catg, i_servingsize, m_servingsize, cal, fat, carb, prot):
        ingredient = self.create(brand=brand,
                category=catg,
                i_serving_size=i_servingsize,
                m_serving_size=m_servingsize,
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
    i_serving_size = models.IntegerField(default=0)
    m_serving_size = models.IntegerField(default=0)
    calories = models.IntegerField()
    fat = models.IntegerField()
    carbohydrates = models.IntegerField()
    protein = models.IntegerField()

    objects = IngredientManager()

    def __str__(self):
        return self.name

