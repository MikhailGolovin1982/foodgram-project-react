# Generated by Django 4.1.1 on 2022-10-23 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_alter_favorite_recipe_alter_favorite_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'verbose_name': 'Закупка по рецепту', 'verbose_name_plural': 'Закупки по рецептам'},
        ),
    ]