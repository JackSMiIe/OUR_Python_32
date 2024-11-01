# Generated by Django 5.1.2 on 2024-10-29 15:17

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, verbose_name='Name')),
                ('status', models.IntegerField(choices=[(1, 'Статус 1'), (2, 'Статус 2'), (3, 'Статус 3')], verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('workload', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traffic.person')),
                ('id_street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traffic.street')),
            ],
        ),
    ]
