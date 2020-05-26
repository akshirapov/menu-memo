from django.urls import path
from .views import (
    AboutView,
    RecipeListView,
    RecipeDetailView,
    RecipeCreateView
)

app_name = 'recipes'

urlpatterns = [
    path('', RecipeListView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('recipes/', RecipeListView.as_view(), name='recipes'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='detail'),
    path('recipe/new/', RecipeCreateView.as_view(), name='create'),
]
