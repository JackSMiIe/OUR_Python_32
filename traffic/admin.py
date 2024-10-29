

from django.contrib import admin
from .models import Person, Street, Journey  # Импорт моделей

# Регистрация моделей в админке
admin.site.register(Person)
admin.site.register(Street)
admin.site.register(Journey)
