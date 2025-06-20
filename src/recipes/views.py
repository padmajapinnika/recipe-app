from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import RecipeSearchForm
from .models import Recipe
import pandas as pd
from .utils import get_chart

@login_required(login_url='login')
def home(request):
    return render(request, 'recipes/recipes_home.html')

@login_required(login_url='login')
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

@login_required(login_url='login')
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

@login_required(login_url='login')
def recipe_search(request):
    form = RecipeSearchForm(request.GET or None)
    chart = None
    recipes = Recipe.objects.none()

    if form.is_valid():
        query = form.cleaned_data.get('query')  # Search text
        chart_type = form.cleaned_data.get('chart_type')

        if query:
            # Filter by title or ingredient name (case-insensitive)
            recipes = Recipe.objects.filter(
                Q(title__icontains=query) |
                Q(recipe_ingredients__ingredient__name__icontains=query)
            ).distinct()
        else:
            recipes = Recipe.objects.all()

        # Generate chart if requested and recipes exist
        if chart_type and recipes.exists():
            # Convert queryset to DataFrame for chart generation
            df = pd.DataFrame(recipes.values('id', 'title', 'cooking_time', 'difficulty'))
            chart = get_chart(chart_type, df)

    context = {
        'form': form,
        'recipes': recipes,
        'chart': chart,
    }
    return render(request, 'recipes/recipe_list.html', context)
