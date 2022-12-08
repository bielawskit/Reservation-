from django.db import migrations


def create_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')

    Group.objects.create(name='clubs')
    Group.objects.create(name='players')


def delete_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')

    Group.objects.get(name='clubs'.delete)
    Group.objects.get(name='players'.delete)


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups, delete_groups)
    ]
