# Generated by Django 3.2.16 on 2023-02-10 13:00

from django.db import migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_superuser'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', users.models.CustomUserManager()),
            ],
        ),
    ]
