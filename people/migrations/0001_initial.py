# Generated by Django 4.2.16 on 2024-09-26 06:20

from django.db import migrations, models
import django.db.models.deletion
import people.form_validation
import university.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('designation', models.CharField(default='Lecturer', max_length=50)),
                ('age', models.IntegerField(validators=[university.models.age_validator])),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('course', models.ManyToManyField(blank=True, to='university.courses')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.departments')),
            ],
            options={
                'ordering': ['department', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('registration_id', models.CharField(max_length=8, unique=True, validators=[people.form_validation.registration_validator])),
                ('date_of_birth', models.DateTimeField()),
                ('password', models.CharField(default='1234', max_length=500)),
                ('course', models.ManyToManyField(blank=True, to='university.courses')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.departments')),
            ],
            options={
                'ordering': ['department', 'registration_id'],
            },
        ),
    ]
