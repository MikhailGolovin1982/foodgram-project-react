from django.contrib import admin
from .models import (Recipe, Ingredient, QuantityIngredient)


admin.site.register(Ingredient)
admin.site.register(QuantityIngredient)
admin.site.register(Recipe)
