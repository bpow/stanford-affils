# Generated by Django 5.0.7 on 2024-07-24 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("affiliations", "0004_rename_cdwg_affiliation_clinical_domain_working_group"),
    ]

    operations = [
        migrations.RenameField(
            model_name="affiliation",
            old_name="name",
            new_name="abbreviated_name",
        ),
        migrations.AddField(
            model_name="affiliation",
            name="full_name",
            field=models.CharField(default=""),
            preserve_default=False,
        ),
    ]
