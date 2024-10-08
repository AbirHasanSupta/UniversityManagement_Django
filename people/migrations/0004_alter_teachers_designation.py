# Generated by Django 4.2.16 on 2024-09-26 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_alter_teachers_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='designation',
            field=models.CharField(choices=[('teaching_assistant', 'Teaching Assistant'), ('lecturer', 'Lecturer'), ('assistant_professor', 'Assistant Professor'), ('associate_professor', 'Associate Professor'), ('professor', 'Professor')], default='lecturer', max_length=50),
        ),
    ]
