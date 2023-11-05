# Generated by Django 4.2.3 on 2023-11-05 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_remove_systemuser_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='systemuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
