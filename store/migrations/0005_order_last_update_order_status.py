# Generated by Django 4.1.2 on 2023-02-08 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_collection_parent_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed'), ('in_progress', 'In Progress'), ('canceled', 'Canceled')], default='pending', max_length=55),
        ),
    ]
