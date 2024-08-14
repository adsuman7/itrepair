# Generated by Django 4.2.6 on 2023-11-25 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                (
                    "phone_number",
                    models.CharField(blank=True, default="", max_length=15, null=True),
                ),
                ("address", models.TextField(blank=True, default="", null=True)),
                ("city", models.TextField(blank=True, default="", null=True)),
                ("state", models.TextField(blank=True, default="", null=True)),
                ("zips", models.TextField(blank=True, default="", null=True)),
                (
                    "user",
                    models.OneToOneField(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Device",
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
                ("brand", models.CharField(max_length=100)),
                (
                    "problem_kind",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("others", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "device_type",
                    models.CharField(
                        choices=[
                            ("mobile", "Mobile"),
                            ("pc", "PC"),
                            ("tablet", "Tablet"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer.customer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DevicePrice",
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
                (
                    "types",
                    models.CharField(
                        choices=[
                            ("mobile", "Mobile"),
                            ("laptop", "Laptop"),
                            ("desktop", "Desktop"),
                            ("tablet", "Tablet"),
                        ],
                        max_length=10,
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer.device",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Bill",
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
                ("issue_description", models.TextField()),
                ("repair_notes", models.TextField(blank=True, null=True)),
                ("total_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer.customer",
                    ),
                ),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer.device",
                    ),
                ),
            ],
        ),
    ]
