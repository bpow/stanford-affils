# Generated by Django 5.0.7 on 2024-07-24 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("affiliations", "0006_alter_affiliation_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="affiliation",
            name="status",
            field=models.CharField(blank=True),
        ),
    ]
