# Generated by Django 4.1.2 on 2023-01-15 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('otp', '0002_OTP_add_validator_phone_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OTP',
        ),
    ]