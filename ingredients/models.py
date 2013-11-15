from django.db import models
from utils.util import in_ttuple


def class_default(str):
    if str == 'category':
        return Category.objects.all()[0]
    elif str == 'brand':
        return Brand.objects.all()[0]
    else:
        return Ingredient.objects.all()[0]


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
    UNITS = (
            ('g', 'gram'),
            ('mL', 'millileter'),
            ('oz', 'ounce'),
            ('unit', 'unit'),
            ('scoop', 'scoop'),
            ('c', 'cup'),
            ('tbsp', 'tbsp'),
            ('tsp', 'tsp'),
            ('unknown', 'unknown'),
    )
    name = models.CharField(max_length=128)
    brand = models.ForeignKey(Brand, default=class_default('brand'))
    category = models.ForeignKey(Category, default=class_default('category'))
    default_serving_size = models.IntegerField()
    default_serving_unit = models.CharField(max_length=15, choices=UNITS, default='unit')
    alt_serving_size = models.IntegerField(default=0)
    alt_serving_unit = models.CharField(max_length=15, choices=UNITS, default='unknown')
    calories = models.IntegerField()
    fat = models.IntegerField()
    carbohydrates = models.IntegerField()
    protein = models.IntegerField()

    objects = IngredientManager()

    def __str__(self):
        return self.name

class MealPartManager(models.Manager):
    def create_mealpart(self, mealid, ingredientid, amount, unit):
        if not Meal.objects.filter(id=mealid) or not Meal.objects.filter(id=ingredientid) or not in_ttuple(MealPart.UNITS, unit):
            return False
        else:
            i = Ingredient.objects.get(id=ingredientid)
            return self.create(mealid=mealid, ingredient=i, amount=amount, unit=unit)


class MealManager(models.Manager):
    def create_meal(self, name, description):
        m = self.create(name=name,
                description=description
                )
        return m

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



class IngredientView(models.Model):
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

    def __str__(self):
        s  = "ID: %s\n" % self.id
        s += "Ingredient: %s\n" % self.ingredient_name
        s += "Brand: %s\n" % self.brand_name
        s += "Category: %s\n" % self.category_name
        s += "DefServ: %s\n" % self.default_serving_size
        s += "DefUnit: %s\n" % self.default_serving_unit
        s += "AltServ: %s\n" % self.alt_serving_size
        s += "AltUnit: %s\n" % self.alt_serving_unit
        s += "Calories: %s\n" % self.calories
        s += "Fat: %s\n" % self.fat
        s += "Carbohydrates: %s\n" % self.carbohydrates
        s += "Protein: %s\n" % self.protein
        return s
    class Meta:
        managed = False

