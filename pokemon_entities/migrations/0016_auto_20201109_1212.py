# Generated by Django 2.2.3 on 2020-11-09 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0015_auto_20201108_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='element_type',
            field=models.ManyToManyField(blank=True, to='pokemon_entities.PokemonElementType', verbose_name='Типы стихий'),
        ),
    ]
