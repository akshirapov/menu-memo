from django.shortcuts import render
from django.views import generic
from .models import Recipe


def home(request):
    return render(request, 'recipes/home.html')


def about(request):
    return render(request, 'recipes/about.html', {'title': 'About'})


class RecipeListView(generic.ListView):
    template_name = 'recipes/recipes.html'
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Recipes'
        return context

    def get_queryset(self):
        return Recipe.objects.all()


class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'
