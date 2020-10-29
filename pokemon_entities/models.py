from django.db import models


class Pokemon(models.Model):
    title = models.CharField('название', max_length=200,)
