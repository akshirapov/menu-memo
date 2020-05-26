from django.urls import reverse_lazy
from django.views import generic

from .models import Recipe
from .forms import RecipeCreateForm


class AboutView(generic.TemplateView):
    """
    A view for displaying a description of a site.
    """
    template_name = 'recipes/about.html'


class RecipeListView(generic.ListView):
    """
    A view for displaying a list of recipes.
    """
    model = Recipe
    template_name = 'recipes/recipes.html'
    context_object_name = 'recipes'
    ordering = ['name']


class RecipeDetailView(generic.DetailView):
    """
    A view for displaying a recipe.
    """
    model = Recipe
    template_name = 'recipes/detail.html'


class RecipeCreateView(generic.CreateView):
    """
    A view for creating a new recipe.
    """
    form_class = RecipeCreateForm
    template_name = 'recipes/new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('recipes:detail', kwargs={'pk': self.object.pk})
