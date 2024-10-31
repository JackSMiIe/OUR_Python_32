from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.db import models

class Person(models.Model):
    username = models.CharField(max_length=30, verbose_name='Name')
    status = models.IntegerField(
        choices=[
            (1, '1'),
            (2, '2'),
            (10, '10')
        ],
        verbose_name='Status'
    )

    def __str__(self):
        return self.username

    def get_status(self):
        return self.status


class Street(models.Model):
    name = models.CharField(max_length=50)
    workload = models.IntegerField(validators=[MaxValueValidator(10)], default=0)  # Изначально 0

    def __str__(self):
        return self.name

    def get_workload(self):
        return self.workload

    def add_person(self, person):
        """Добавляет человека на улицу и обновляет уровень загруженности"""
        if person.status == 10:
            # Если статус 10, сбрасываем других людей и устанавливаем загруженность на 10
            self.workload = 10
            self.save()
            # Удаляем всех других пользователей с этой улицы
            Journey.objects.filter(id_street=self).exclude(id_person=person).delete()
        else:
            # Проверяем, не превышает ли суммарная загруженность 10
            if self.workload + person.status > 10:
                raise ValidationError("Невозможно добавить, загруженность превысит лимит.")
            # Добавляем статус человека к текущей загруженности
            self.workload += person.status
            self.save()

    def remove_person(self, person):
        """Удаляет человека с улицы и обновляет уровень загруженности"""
        if self.workload - person.status >= 0:
            self.workload -= person.status
        else:
            self.workload = 0  # Защита от отрицательных значений
        self.save()


class Journey(models.Model):
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    id_street = models.ForeignKey(Street, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Перед сохранением проверяем условия и добавляем человека на улицу
        self.id_street.add_person(self.id_person)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # При удалении удаляем человека с улицы
        self.id_street.remove_person(self.id_person)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"По улице {self.id_street} едет {self.id_person} с статусом {self.id_person.get_status_display()}"
