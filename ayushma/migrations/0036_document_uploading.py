# Generated by Django 4.2.1 on 2023-08-09 16:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ayushma", "0035_auto_20230731_1407"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="uploading",
            field=models.BooleanField(default=False),
        ),
    ]