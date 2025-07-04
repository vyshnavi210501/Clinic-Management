# Generated by Django 5.2 on 2025-06-02 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_remove_clinic_working_hours_clinic_closing_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='closing_time',
            field=models.TimeField(default='18:00:00', max_length=20),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='opening_time',
            field=models.TimeField(default='09:00:00', max_length=20),
        ),
    ]
