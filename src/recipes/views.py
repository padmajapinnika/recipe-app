from django.shortcuts import render, get_object_or_404
from .models import Recipe

def home(request):
    return render(request, 'recipes/recipes_home.html')

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    # No need for extra query if related_name is set properly
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
