# Generated by Django 4.2.6 on 2023-12-04 04:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customer", "0007_appointments_timeframe"),
    ]

    operations = [
        migrations.AlterField(
            model_name="timeframe",
            name="timeframe",
            field=models.CharField(
                choices=[
                    ("SEVEN", "7:00 AM"),
                    ("EIGHT", "8:00 AM"),
                    ("NINE", "9:00 AM"),
                    ("TEN", "10:00 AM"),
                    ("ELEVEN", "11:00 AM"),
                    ("TWELVE", "12:00 PM"),
                    ("THIRTEEN", "1:00 PM"),
                    ("FOURTEEN", "2:00 PM"),
                    ("FIFTEEN", "3:00 PM"),
                    ("SIXTEEN", "4:00 PM"),
                    ("SEVENTEEN", "5:00 PM"),
                ],
                max_length=10,
            ),
        ),
    ]
