# Generated by Django 4.2 on 2023-05-23 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aid_app', '0004_doctor_fieldspecialist'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fieldname', models.CharField(max_length=45)),
                ('doctor_pic', models.FileField(default='', upload_to='Aid_app/doctorpic')),
                ('specialization', models.CharField(max_length=55)),
                ('description', models.TextField(default='')),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Aid_app.doctor')),
            ],
        ),
    ]
