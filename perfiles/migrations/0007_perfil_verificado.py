# Generated by Django 4.2 on 2023-04-08 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0006_perfil_carrera'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='verificado',
            field=models.BooleanField(default=False),
        ),
    ]
