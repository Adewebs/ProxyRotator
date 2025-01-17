# Generated by Django 5.0.1 on 2024-01-13 06:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("proxyapp", "0002_proxy_information"),
    ]

    operations = [
        migrations.CreateModel(
            name="ScrapeURL",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.URLField(unique=True)),
            ],
        ),
    ]
