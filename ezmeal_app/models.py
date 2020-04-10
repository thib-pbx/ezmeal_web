from django.db import models
from django.utils.translation import gettext_lazy as _

class Ingredients(models.Model):

    class UnitChoices(models.TextChoices):
        WEIGHT = 'WEIGHT', _('g', 'kg')
        VOLUME = 'VOLUME', _('L', 'cL', 'mL')
        COUNT = 'COUNT', _('Unité')
        UNCOUNTABLE = 'UNCOUNTABLE', _('Autre')
    class Category(models.TextChoices):
        INGREDIENTS = 'Aliments'
        OTHER = 'Autre'
    name = models.CharField(max_length=40)
    unit = models.CharField(
        max_length=20,
        choices=UnitChoices.choices)
    category = models.CharField(
        max_length=40,
        choices=Category.choices)

class Recipes(models.Model):
    name = models.CharField(max_length=40)
    nb_ppl = models.IntegerField()
    prep_tips = models.TextField(max_length=1000)

class IngredientsInRecipe(models.Model):
    recipe_id = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.FloatField(max_length=10)

class Weeks(models.Model):
    name = models.CharField(max_length=40)

class RecipesInWeek(models.Model):
    week_id = models.ForeignKey(Weeks, on_delete=models.CASCADE)
    day_id = models.PositiveSmallIntegerField()
    meal_id = models.PositiveSmallIntegerField()
    recipe_id = models.ForeignKey(Recipes, on_delete=models.CASCADE)




