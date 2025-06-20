from django.urls import path
from .views import home, recipe_list, recipe_detail, recipe_search
from recipe_project.views import login_view, logout_view

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),  
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('list/', recipe_list, name='recipe_list'),
    path('detail/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('search/', recipe_search, name='recipe_search'),
]
