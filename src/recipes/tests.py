from django.test import TestCase
from .models import Recipe

class RecipeModelTest(TestCase):

    def setUp(self):
        # Set up a sample recipe object to use in tests
        self.recipe = Recipe.objects.create(
            name="Pancakes",
            ingredients="flour, milk, eggs, sugar",
            cooking_time=15
        )

    def test_recipe_str(self):
        # Test the string representation returns the name
        self.assertEqual(str(self.recipe), "Pancakes")

    def test_get_ingredient_list(self):
        # Test that get_ingredient_list splits ingredients correctly and strips whitespace
        expected_ingredients = ["flour", "milk", "eggs", "sugar"]
        self.assertEqual(self.recipe.get_ingredient_list(), expected_ingredients)

    def test_cooking_time_positive(self):
        # cooking_time should be positive; Django model enforces this, but you can still check value type
        self.assertTrue(self.recipe.cooking_time > 0)
