from django.core.validators import MaxValueValidator
from django.db import models

class Person(models.Model):
    username = models.CharField(max_length=30, verbose_name='Name')
    status = models.IntegerField(
        choices=[
            (1, 'Статус 1'),
            (2, 'Статус 2'),
            (3, 'Статус 3')
        ],
        verbose_name='Status'
    )

    def __str__(self):
        return self.username

    def get_status(self):
        return self.status


class Street(models.Model):
    name = models.CharField(max_length=50)
    workload = models.IntegerField(validators=[MaxValueValidator(10)])

    def __str__(self):
        return self.name

    def get_workload(self):
        return self.workload

    def set_up_workload(self, status):
        self.workload += status
        self.save()

    def set_down_workload(self, status):
        self.workload -= status
        self.save()

    def set_vip_person(self):
        self.workload = 0
        self.save()


class Journey(models.Model):
    id_person = models.ForeignKey(Person, on_delete=models.CASCADE)
    id_street = models.ForeignKey(Street, on_delete=models.CASCADE)
    status = models.IntegerField(
        choices=[
            (1, 'Статус 1'),
            (2, 'Статус 2'),
            (10, 'Статус 10')
        ],
        default=1,
        verbose_name='Status'
    )

    def __str__(self):
        return f"По улице {self.id_street} едет {self.id_person} с статусом {self.get_status_display()}"
