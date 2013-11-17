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
    def create_ingredient_from_form(self, f):
        name = f.cleaned_data.get('name')
        brand = f.cleaned_data.get('brand')
        catg = f.cleaned_data.get('category')
        dss = f.cleaned_data.get('default_serving_size')
        dsu = f.cleaned_data.get('default_serving_unit')
        ass = f.cleaned_data.get('alt_serving_size')
        asu = f.cleaned_data.get('alt_serving_unit')
        calories = f.cleaned_data.get('calories')
        fat = f.cleaned_data.get('fat')
        carbs = f.cleaned_data.get('carbohydrates')
        prot = f.cleaned_data.get('protein')
        print(brand)


    def create_ingredient(self, name, brand, catg, dservingsize, dservingunit, aservingsize, aservingunit, cal, fat, carb, prot):
        if isinstance(brand, str):
            brand = Brand.objects.get(name=brand)
        if isinstance(brand, int):
            brand = Brand.objects.get(id=brand)
        if isinstance(catg, str):
            catg  = Category.objects.get(name=catg)
        if isinstance(catg, int):
            brand = Category.objects.get(id=brand)
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
    default_serving_size = models.DecimalField(max_digits=8, decimal_places=2)
    default_serving_unit = models.CharField(max_length=15, choices=UNITS, default='unit')
    alt_serving_size = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    alt_serving_unit = models.CharField(max_length=15, choices=UNITS, default='unknown')
    calories = models.DecimalField(max_digits=8, decimal_places=2)
    fat = models.DecimalField(max_digits=8, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=8, decimal_places=2)
    protein = models.DecimalField(max_digits=8, decimal_places=2)

    objects = IngredientManager()

    def __str__(self):
        return self.name



class IngredientView(models.Model):
    ingredient_name = models.CharField(max_length=128)
    brand_name = models.CharField(max_length=40)
    category_name = models.CharField(max_length=40)
    default_serving_size = models.DecimalField(max_digits=8, decimal_places=2)
    default_serving_unit = models.CharField(max_length=8)
    alt_serving_size = models.DecimalField(max_digits=8, decimal_places=2)
    alt_serving_unit = models.CharField(max_length=8)
    calories = models.DecimalField(max_digits=8, decimal_places=2)
    fat = models.DecimalField(max_digits=8, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=8, decimal_places=2)
    protein = models.DecimalField(max_digits=8, decimal_places=2)

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
        db_table = 'INGREDIENT_VIEW'

