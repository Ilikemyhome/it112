from django.shortcuts import render, get_object_or_404
from .models import Pets

# Create your views here.

def pet_list(request):
    pets = Pets.objects.all()
    return render(request, 'pet_list.html', {'pets': pets})

def pet_detail(request, pet_id):  
    pet = get_object_or_404(Pets, id=pet_id)
    return render(request, 'pet_detail.html', {'pet': pet})