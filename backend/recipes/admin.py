from django.contrib import admin
from .models import (Recipe, Ingredient, IngredientRecipe, Tag)


admin.site.register(Tag)


class IngredientRecipeInline(admin.TabularInline):
    model = IngredientRecipe
    extra = 1


class IngredientAdmin(admin.ModelAdmin):
    inlines = (IngredientRecipeInline,)


class RecipesAdmin(admin.ModelAdmin):
    inlines = (IngredientRecipeInline,)


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipesAdmin)
