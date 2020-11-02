from django.db import models


class PokemonElementType(models.Model):
    title = models.CharField('название', max_length=50,)
    image = models.ImageField('изображение', blank=True, null=True,)
    strong_against = models.ManyToManyField('self', symmetrical=False,
                                            verbose_name='Силён против',)

    def __str__(self):
        return self.title


class Pokemon(models.Model):
    title = models.CharField('название', max_length=200,)
    title_en = models.CharField('название на англ.', max_length=200, blank=True,)
    title_jp = models.CharField('название на яп.', max_length=200, blank=True,)
    image = models.ImageField('изображение',)
    description = models.TextField('описание', blank=True,)
    element_type = models.ManyToManyField(PokemonElementType)
    previous_evolution = models.ForeignKey('self', on_delete=models.SET_NULL, null=True,
                                           blank=True, verbose_name='Из кого эволюционировал',
                                           related_name='next_evolutions')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField('широта',)
    lon = models.FloatField('долгота',)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE,
                                verbose_name='Покемон', related_name='entities',)
    appeared_at = models.DateTimeField('появление', blank=True, null=True,)
    disappeared_at = models.DateTimeField('исчезновение', blank=True, null=True,)
    level = models.IntegerField('уровень', blank=True, null=True,)
    health = models.IntegerField('здоровье', blank=True, null=True,)
    strength = models.IntegerField('атака', blank=True, null=True,)
    defence = models.IntegerField('защита', blank=True, null=True,)
    stamina = models.IntegerField('выносливость', blank=True, null=True,)
