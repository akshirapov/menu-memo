from django import forms

from .models import Recipe


class RecipeCreateForm(forms.ModelForm):
    """
    A form containing form fields for creating a new recipe.
    """

    class Meta:
        model = Recipe
        exclude = ["author"]
