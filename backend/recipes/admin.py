from django.contrib import admin

from .models import (Favorite, Ingredient, IngredientRecipe, Recipe,
                     ShoppingCart, Tag)


class IngredientRecipeInline(admin.TabularInline):
    model = IngredientRecipe
    extra = 1


class IngredientAdmin(admin.ModelAdmin):
    inlines = (IngredientRecipeInline,)


class RecipesAdmin(admin.ModelAdmin):
    inlines = (IngredientRecipeInline,)
    list_display = (
        'id',
        'name',
        'author',
        'pub_date'
    )


class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'recipe',
    )


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'recipe',
    )


admin.site.register(Tag)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipesAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
