from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField(help_text="Enter the ingredients, separated by a comma")
    cooking_time = models.PositiveIntegerField(help_text="Enter cooking time in minutes")

    def __str__(self):
        return self.name

    def get_ingredient_list(self):
        """
        Returns a list of individual ingredients with whitespace stripped.
        """
        return [i.strip() for i in self.ingredients.split(',') if i.strip()]
