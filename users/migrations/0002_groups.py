import os
from django.db import migrations
from django.db import transaction


@transaction.atomic
def create_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")

    Group.objects.create(name=os.environ.get("DJ_GROUP_CLUBS"))
    Group.objects.create(name=os.environ.get("DJ_GROUP_PLAYERS"))


def delete_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")

    Group.objects.get(name=os.environ.get("DJ_GROUP_CLUBS")).delete()
    Group.objects.get(name=os.environ.get("DJ_GROUP_PLAYERS")).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [migrations.RunPython(create_groups, delete_groups)]
