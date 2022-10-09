from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import UserManager


class User(AbstractUser):
    USER = 'user'
    ADMIN = 'admin'

    ROLE_CHOICES = [
        (USER, 'user'),
        (ADMIN, 'admin'),
    ]

    username = models.CharField(
        'имя пользователя', max_length=150, unique=True)
    email = models.EmailField('адрес электронной почты', unique=True,
                              db_index=True)
    role = models.CharField('права пользователя',
                            max_length=9, choices=ROLE_CHOICES, default='user')
    bio = models.TextField('коротко о себе', max_length=500, blank=True)
    first_name = models.CharField('имя', max_length=150, blank=True)
    last_name = models.CharField('фамилия', max_length=150, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name',]

    class Meta:
        ordering = ['pk']
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser


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
