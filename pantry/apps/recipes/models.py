from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Ingredient(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        db_index=True
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
        default='',
        blank=True
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(640, 480)],
        format='JPEG',
        options={'quality': 60}
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
