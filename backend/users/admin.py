from django.contrib import admin
from .models import (User, Recipe, Ingredient, QuantityIngredient)


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'role',
        'bio',
        'first_name',
        'last_name',
    )

    search_fields = ('username',)
    list_filter = ('email', 'username',)


admin.site.register(User, UserAdmin)

admin.site.register(Ingredient)
admin.site.register(QuantityIngredient)
admin.site.register(Recipe)
