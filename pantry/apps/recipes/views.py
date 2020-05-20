from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipes/index.html', context)


def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context = {'recipe': recipe}
    return render(request, 'recipes/detail.html', context)
