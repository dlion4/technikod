# Generated by Django 4.2.4 on 2024-01-08 11:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0002_tip"),
    ]

    operations = [
        migrations.AddField(
            model_name="tip",
            name="url",
            field=models.URLField(default="https://lionnic.com/", max_length=1000),
            preserve_default=False,
        ),
    ]
