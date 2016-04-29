from django.contrib import admin

from .models import House, Character


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):

    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):

    list_display = ('name', 'house', 'is_lord', 'likes', 'dislikes')
    list_filter = ('house',)
    search_fields = ('name',)
