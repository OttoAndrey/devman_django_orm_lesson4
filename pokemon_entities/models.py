from django.db import models


class Pokemon(models.Model):
    title = models.CharField('название', max_length=200,)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField('широта',)
    lon = models.FloatField('долгота',)
