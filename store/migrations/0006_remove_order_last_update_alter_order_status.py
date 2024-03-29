# Generated by Django 4.1.2 on 2023-02-08 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_order_last_update_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='last_update',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('canceled', 'Canceled'), ('failed', 'Failed'), ("[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed'), ('in_progress', 'In Progress'), ('canceled', 'Canceled')]", 'Choices')], default='pending', max_length=255),
        ),
    ]
