# Generated by Django 4.2.16 on 2024-09-26 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='password',
            field=models.CharField(default='abcd', max_length=500),
        ),
    ]
