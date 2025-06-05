from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Pets
import json

# Create your views here.

def pet_list(request):
    pets = Pets.objects.all()
    return render(request, 'pet_list.html', {'pets': pets})

def pet_detail(request, pet_id):  
    pet = get_object_or_404(Pets, id=pet_id)
    return render(request, 'pet_detail.html', {'pet': pet})

def api_single_pet(request):
    if request.method == 'GET' :
        pet_id = request.GET.get('id')
    
        if not pet_id:
            return JsonResponse({'error': 'Pet ID is required'}, status=200, content_type='application/json')
        try:
            pet = Pets.objects.values().get(id=pet_id)
            return JsonResponse(pet, status=200, content_type='application/json')
        
        except Pets.DoesNotExist:
            return JsonResponse({'error': 'Pet not found'}, status=200, content_type='application/json')
        
def api_all_pets(request):
    if request.method == 'GET':
        pets = Pets.objects.values()
        pets_list = list(pets)
        return JsonResponse(pets_list, safe=False, status=200, content_type='application/json')
    

@csrf_exempt
def api_create_pet(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            pet = Pets.objects.create(
                name = data.get('name'),
                color = data.get('color'),
                age = data.get('age', 0),
                pet_type = data.get('pet_type')
            )
            return JsonResponse({'success': True, 'id': pet.id}, status=200, content_type='application/json')
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=200, content_type='application/json')
    return JsonResponse({'error': 'POST required'}, status=200, content_type='application/json')
