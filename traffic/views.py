from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Street, Person, Journey

def home(request):
    streets = Street.objects.all()
    persons = Person.objects.all()
    error_message = None

    # Добавление человека на улицу (если запрос POST)
    if request.method == 'POST':
        person_id = request.POST.get('person_id')
        street_id = request.POST.get('street_id')

        if person_id and street_id:
            try:
                person = Person.objects.get(id=person_id)
                street = Street.objects.get(id=street_id)
                # Создаем поездку и добавляем человека на улицу
                journey = Journey(id_person=person, id_street=street)
                journey.save()
            except ValidationError as e:
                error_message = str(e)

    return render(request, 'home.html', {
        'streets': streets,
        'persons': persons,
        'error_message': error_message,
    })

def remove_person(request, journey_id):
    journey = Journey.objects.get(id=journey_id)
    journey.delete()
    return redirect('home')
