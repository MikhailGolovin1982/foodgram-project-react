from django.db import models

from users.models import User


class Ingredient(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название ингредиента",
        help_text="Здесь будет указан ингредиент",
    )
    measurement_unit = models.CharField(
        max_length=20,
        verbose_name="Название единиц измерения",
        help_text="Здесь будет указано название единиц измерения",
    )

    def __str__(self):
        return self.name


class QuantityIngredient(models.Model):
    ingredient = models.ForeignKey(
        Ingredient, related_name='ingredients',
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(verbose_name='количество')

    def __str__(self):
        return self.ingredient.name


class Tag(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="Название тэга",
        help_text="Здесь будет указано название тэга",
    )

    slug = models.SlugField(
        unique=True,
        verbose_name="Это слаг, для тэга",
        help_text="К нему потом можно будет обращаться",
    )

    color = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название рецепта",
        help_text="Здесь будет указано название рецепта",
    )
    description = models.TextField(
        max_length=1000,
        verbose_name="Описание рецепта",
        help_text="Здесь будет указано описание рецепта",
    )

    ingredient = models.ManyToManyField(
        QuantityIngredient,
        related_name='quantity_ingredient',
        verbose_name="Ингредиент рецепта",
        help_text="Ингредиент рецепта",
    )

    tag = models.ManyToManyField(
        Tag,
        related_name='tags',
        verbose_name="Тэг",
        help_text="Тэг рецепта",
    )

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipes')

    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return self.name
