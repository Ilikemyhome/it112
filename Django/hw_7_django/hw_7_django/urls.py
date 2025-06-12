"""
URL configuration for hw_7_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home
from pets.views import pet_list, pet_detail, api_all_pets, api_single_pet, api_create_pet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    
    path('pets/', pet_list, name='pet_list'),
    path('pets/<int:pet_id>/', pet_detail, name='pet_detail'),

    path('api/pets/', api_all_pets, name='api_all_pets'),
    path('api/pet/', api_single_pet, name='api_single_pet'),
    path('api/create_pet/', api_create_pet, name='api_create_pet'),
]
