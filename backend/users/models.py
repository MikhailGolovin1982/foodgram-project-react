from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .manager import UserManager


# Create your models here.
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
    confirm = models.CharField('код подтверждения', max_length=200, blank=True)
    first_name = models.CharField('имя', max_length=150, blank=True)
    last_name = models.CharField('фамилия', max_length=150, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    class Meta:
        ordering = ['pk']
        verbose_name = "пользователь"

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser
