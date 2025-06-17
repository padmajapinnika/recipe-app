from django.urls import path
from .views import home, recipe_list, recipe_detail

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),          # Welcome page
    path('list/', recipe_list, name='recipe_list'),  # Recipes overview page
    path('detail/<int:pk>/', recipe_detail, name='recipe_detail'),
]