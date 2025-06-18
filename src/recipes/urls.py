from django.urls import path
from .views import home, recipe_list, recipe_detail 
from recipe_project.views import login_view, logout_view

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),  
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('list/', recipe_list, name='recipe_list'),  # Recipes overview page
    path('detail/<int:pk>/', recipe_detail, name='recipe_detail'),
]