# Generated by Django 4.2.16 on 2024-09-25 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0005_teachers_designation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachers',
            name='course',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='department',
        ),
        migrations.DeleteModel(
            name='Students',
        ),
        migrations.DeleteModel(
            name='Teachers',
        ),
    ]
