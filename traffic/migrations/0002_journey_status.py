# Generated by Django 5.1.2 on 2024-10-29 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='status',
            field=models.IntegerField(choices=[(1, 'Статус 1'), (2, 'Статус 2'), (10, 'Статус 10')], default=1, verbose_name='Status'),
        ),
    ]