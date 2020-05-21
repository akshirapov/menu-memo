from django.db import models


class Ingredient(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        db_index=True
    )
    image = models.ImageField(
        upload_to='ingredients',
        default='default.jpg',
        blank=True
    )
    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'ingredients'


class Recipe(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        db_index=True
    )
    image = models.ImageField(
        upload_to='recipes',
        default='default.jpg',
        blank=True
    )
    description = models.TextField(
        blank=True
    )
    method = models.TextField(
        blank=True
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'recipes'
