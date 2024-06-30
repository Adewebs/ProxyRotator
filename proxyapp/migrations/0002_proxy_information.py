# Generated by Django 5.0.1 on 2024-01-13 06:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("proxyapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Proxy_information",
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
                ("ip", models.GenericIPAddressField()),
                ("port", models.PositiveIntegerField()),
                ("username", models.CharField(max_length=50)),
                ("password", models.CharField(max_length=50)),
            ],
        ),
    ]
