# Generated by Django 4.2 on 2023-04-29 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_remove_employee_password_remove_restaurant_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
