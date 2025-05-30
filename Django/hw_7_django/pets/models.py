from django.db import models

class Pets(models.Model):
    COMMON_PETS = [
        ('ct', 'Cat'),
        ('dg', 'Dog'),
        ('hmtr', 'Hamster'),
        ('prrt', 'Parrot'),
        ('fsh', 'Fish'),
        ('other', 'Other')
    ]
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    age = models.PositiveIntegerField(blank=True)
    pet_type = models.CharField(max_length=20, choices=COMMON_PETS)

    def __str__(self):
        return f"{self.name} ({self.get_pet_type_display()}) - {self.color}, {self.age} years old"