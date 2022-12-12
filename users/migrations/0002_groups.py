import os
from django.db import migrations


def create_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')

    Group.objects.create(name=os.environ.get('DJ_GROUP_clubs'))
    Group.objects.create(name=os.environ.get('DJ_GROUP_players'))


def delete_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')

    Group.objects.get(name=os.environ.get('DJ_GROUP_clubs').delete)
    Group.objects.get(name=os.environ.get('DJ_GROUP_players').delete)


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups, delete_groups)
    ]
