from typing import Any
from django.db import migrations
from django.contrib.auth.models import Group, Permission

DEFAULT_ROLES = {
    "candidate": [], 
    "recruiter": ["add_vacancy", "add_company"]
}


def populate_db_with_default_roles(apps: Any, schema_editor: Any) ->None:
    for role_name, permissions_list in DEFAULT_ROLES.items():
        group = Group.objects.create(name=role_name)
        permissions = Permission.objects.filter(codename__in=permissions_list)
        group.permissions.set(permissions)


def drop_default_roles_from_db(apps:Any, schema_editor: Any) -> None:
    for role_name in DEFAULT_ROLES:
        Group.objects.get(name=role_name).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_company_logo'),
    ]

    operations = [
        migrations.RunPython(
            code=populate_db_with_default_roles,
            reverse_code=drop_default_roles_from_db,
        )
    ]
