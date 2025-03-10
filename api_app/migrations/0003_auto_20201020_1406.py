# Generated by Django 2.2.14 on 2020-10-20 14:06

from django.db import migrations
from datetime import timedelta


def create_default_clients(apps, schema_editor):
    # We can't import the Client model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Client = apps.get_model("durin", "Client")
    # for pyintelowl, custom token_ttl
    Client.objects.update_or_create(
        name="pyintelowl", token_ttl=timedelta(weeks=4 * 12 * 10)
    )
    # others, default token_ttl
    Client.objects.update_or_create(name="web-browser")


class Migration(migrations.Migration):

    dependencies = [
        ("api_app", "0002_added_job_field"),
        # added dependency to enable using models from app2 in move_m1
        ("durin", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_default_clients, migrations.RunPython.noop)
    ]
