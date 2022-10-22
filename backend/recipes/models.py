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

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"

    def __str__(self):
        return self.name


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

    color = models.CharField(max_length=7)

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название рецепта",
        help_text="Здесь будет указано название рецепта",
    )
    text = models.TextField(
        max_length=1000,
        verbose_name="Описание рецепта",
        help_text="Здесь будет указано описание рецепта",
    )

    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientRecipe',
        related_name='recipe_ingredient',
        verbose_name='Ингредиенты рецепта',
        help_text='Ингредиенты рецепта',
    )

    tags = models.ManyToManyField(
        Tag,
        related_name='tags',
        verbose_name='Тэг',
        help_text='Тэг рецепта',
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор рецепта'
    )

    cooking_time = models.IntegerField(
        verbose_name='Время приготовления',
        help_text='Укажите время приготовления в минутах'
    )

    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True
    )

    image = models.ImageField(
        upload_to='recipes/images/',
        null=True,
        default=None
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class IngredientRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_ingredients')
    ingredient = models.ForeignKey(Ingredient,  on_delete=models.CASCADE, related_name='ingredients')
    amount = models.IntegerField('Количество')

    class Meta:
        verbose_name = 'Ингредиенты рецептов'
        verbose_name_plural = 'Ингредиенты рецептов'

    def __str__(self):
        return f'{self.ingredient.name} - {self.amount} - {self.ingredient.measurement_unit}'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='User',
        help_text='Choose the user'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Recipe',
        help_text='Choose the recipe'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique favorite'
            )
        ]
        verbose_name = 'Любимый рецепт'
        verbose_name_plural = 'Любимые рецепты'

    def __str__(self):
        return f'--{self.user}-- likes the recipe --{self.recipe}--'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='User',
        help_text='Choose the user'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Recipe',
        help_text='Choose the recipe'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique shopping_cart'
            )
        ]
        verbose_name = 'Закупка по рецепту'
        verbose_name_plural = 'Закупки по рецептам'

    def __str__(self):
        return f'--{self.user}-- wants to buy ingredients from the recipe --{self.recipe}--'


