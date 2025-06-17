from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Ingredient, RecipeIngredient

class TestRecipeModel(TestCase):
    def setUp(self):
        self.ingredient1 = Ingredient.objects.create(name="Salt")
        self.ingredient2 = Ingredient.objects.create(name="Pepper")

        self.recipe = Recipe.objects.create(
            title="Simple Dish",
            description="Just a test recipe.",
            cooking_time=5,
            pic="test_pic.jpg"
        )
        RecipeIngredient.objects.create(recipe=self.recipe, ingredient=self.ingredient1)
        RecipeIngredient.objects.create(recipe=self.recipe, ingredient=self.ingredient2)

    def test_recipe_str(self):
        self.assertEqual(str(self.recipe), "Simple Dish")

    def test_ingredient_str(self):
        self.assertEqual(str(self.ingredient1), "Salt")

    def test_recipe_ingredient_str(self):
        relation = RecipeIngredient.objects.get(recipe=self.recipe, ingredient=self.ingredient1)
        self.assertEqual(str(relation), "Salt in Simple Dish")

    def test_calculate_difficulty_easy(self):
        self.assertEqual(self.recipe.calculate_difficulty(), "Easy")

    def test_recipe_has_correct_ingredients(self):
        self.assertEqual(self.recipe.ingredients.count(), 2)

    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipes:recipe_list'))  # Note 'recipes:' prefix
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Simple Dish")

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipes:recipe_detail', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Just a test recipe.")

    def test_home_view(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
