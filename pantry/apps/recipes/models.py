from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Ingredient(models.Model):
    name = models.CharField(
        max_length=255,
        db_index=True, unique=True
    )
    image = ProcessedImageField(
        upload_to='ingredients',
        default='default.jpg',
        processors=[ResizeToFill(1024, 768)],
        format='JPEG',
        options=[{'quality': 60}]
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
        db_index=True
    )

    image = ProcessedImageField(
        upload_to='recipes',
        default='default.jpg',
        processors=[ResizeToFill(1024, 768)],
        format='JPEG',
        options=[{'quality': 60}]
    )
    description = models.TextField(
        blank=True
    )
    method = models.TextField(
        blank=True
    )
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'recipes'
