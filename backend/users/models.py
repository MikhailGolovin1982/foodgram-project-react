from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import UserManager
# from recipes.models import Recipe, Ingredient, QuantityIngredient


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


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='User',
        help_text='Choose following user'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Author',
        help_text='Choose author to follow'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique follow'
            )
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'--{self.user}-- is subscribed to --{self.following}--'

