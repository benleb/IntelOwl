# Generated by Django 3.2.4 on 2021-07-28 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_app", "0008_remove_job_runtime_configuration"),
        ("connectors_manager", "0007_connectorreport_task_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="connectorreport", old_name="connector_name", new_name="name"
        ),
        migrations.AddField(
            model_name="connectorreport",
            name="runtime_configuration",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterUniqueTogether(
            name="connectorreport", unique_together={("name", "job")}
        ),
    ]
