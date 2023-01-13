# Generated by Django 4.1.2 on 2023-01-11 20:07

from django.db import migrations, models
import otp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('otp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='phone_number',
            field=models.CharField(max_length=11, validators=[otp.validators.validate_phone_number_format]),
        ),
    ]