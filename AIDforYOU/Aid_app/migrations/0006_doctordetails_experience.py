# Generated by Django 4.2 on 2023-05-23 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aid_app', '0005_doctordetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctordetails',
            name='experience',
            field=models.TextField(default=''),
        ),
    ]
