# Generated by Django 4.1.2 on 2023-02-05 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_password'),
        ('store', '0004_collection_parent_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.customer'),
        ),
    ]
