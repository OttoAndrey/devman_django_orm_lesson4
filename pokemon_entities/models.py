from django.db import models


class Pokemon(models.Model):
    title = models.CharField('название', max_length=200,)
    title_en = models.CharField('название на англ.', max_length=200, blank=True,)
    title_jp = models.CharField('название на яп.', max_length=200, blank=True,)
    image = models.ImageField('изображение',)
    description = models.TextField('описание', blank=True,)
    previous_evolution = models.ForeignKey('self', on_delete=models.SET_NULL,
                                           null=True, default=None, verbose_name='Из кого эволюционировал',)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField('широта',)
    lon = models.FloatField('долгота',)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE,
                                verbose_name='Покемон', related_name='entities',)
    appeared_at = models.DateTimeField('появление',)
    disappeared_at = models.DateTimeField('исчезновение',)
    level = models.IntegerField('уровень',)
    health = models.IntegerField('здоровье',)
    strength = models.IntegerField('атака',)
    defence = models.IntegerField('защита',)
    stamina = models.IntegerField('выносливость',)
