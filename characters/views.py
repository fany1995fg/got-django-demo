from django.shortcuts import render, get_object_or_404

from .models import House


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
