from django.urls import path
from . import views
from .views import (
    RecipeListView,
    RecipeDetailView
)

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('recipes/', RecipeListView.as_view(), name='recipes'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='detail'),
]
