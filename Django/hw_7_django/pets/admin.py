from django.contrib import admin
from .models import Pets

# Register your models here.

@admin.register(Pets)
class PetsAdmin(admin.ModelAdmin):
    search_fields = ['name', 'color']
    list_display = ['name', 'color', 'age', 'pet_type']
    list_filter = ['pet_type']