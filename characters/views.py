from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect

from .models import House, Character


def home(request):
    houses = House.objects.all()
    return render(request, 'characters/home.html', {
        'houses': houses
    })


def house_detail(request, house_id):
    house = get_object_or_404(House, id=house_id)
    return render(request, 'characters/house_detail.html', {
        'house': house
    })


def character_action(request, house_id, character_id, action):
    character = get_object_or_404(Character, id=character_id)
    if action == 'like':
        character.likes += 1
    else:
        character.dislikes += 1
    character.save()
    return redirect(reverse('house_detail', kwargs={'house_id': house_id}))
