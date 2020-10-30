# Generated by Django 2.2.3 on 2020-10-30 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0008_auto_20201030_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pokemon_entities.Pokemon', verbose_name='Из кого эволюционировал'),
        ),
    ]