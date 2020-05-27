from django.db import models
from django.contrib.auth.models import User

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Ingredient(models.Model):
    """
    Represents the ingredient model.
    """
    name = models.CharField(
        max_length=128,
        unique=True,
        db_index=True
    )

    class Meta:
        verbose_name_plural = 'ingredients'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """
    Represents the recipe model.
    """
    name = models.CharField(
        max_length=128,
        unique=True,
        db_index=True
    )
    author = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    image = models.ImageField(
        blank=True,
        upload_to='recipes',
        default=''
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
    ingredients = models.ManyToManyField(
        Ingredient,
        blank=True,
    )
    method = models.TextField(
        blank=True
    )

    class Meta:
        verbose_name_plural = 'recipes'

    def __str__(self):
        return self.name
