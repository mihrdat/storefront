# Generated by Django 4.1.2 on 2023-04-04 08:41

from django.db import migrations
import user.models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0005_alter_customer_user"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", user.models.UserManager()),
            ],
        ),
    ]
