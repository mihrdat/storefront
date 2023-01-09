# Generated by Django 4.1.2 on 2023-01-09 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import otp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration_time', models.DateTimeField(default=otp.models.set_expiration_time)),
                ('code', models.CharField(default=otp.models.generate_random_code, max_length=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]