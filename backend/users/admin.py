from django.contrib import admin
from .models import (User, Recipe, Ingredient, QuantityIngredient)

admin.site.register(User)
admin.site.register(Ingredient)
admin.site.register(QuantityIngredient)
admin.site.register(Recipe)
