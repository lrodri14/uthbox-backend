# Generated by Django 4.2 on 2023-04-07 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archivos', '0002_archivo_creado_por'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivo',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
