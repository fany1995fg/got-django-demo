from __future__ import unicode_literals

from django.db import models


class House(models.Model):

    name = models.CharField('Name', max_length=100)
    logo = models.ImageField('Logo', upload_to='families/logos/')

    def __str__(self):
        return self.name


class Character(models.Model):

    house = models.ForeignKey('House', related_name='characters')
    name = models.CharField('Name', max_length=200)
    is_lord = models.BooleanField('Is lord?', default=False)
    image = models.ImageField('Logo', upload_to='characters/images/')
    likes = models.PositiveIntegerField('Likes', default=0, blank=True)
    dislikes = models.PositiveIntegerField('Likes', default=0, blank=True)
    dislikes_quantity_to_die = models.PositiveIntegerField('Dislikes to die', help_text='Min quantity of dislikes quantity to die')

    def __str__(self):
        return self.name
