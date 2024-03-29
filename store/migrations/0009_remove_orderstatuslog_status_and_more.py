# Generated by Django 4.1.2 on 2023-02-12 21:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0008_merge_20230210_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderstatuslog',
            name='status',
        ),
        migrations.AddField(
            model_name='orderstatuslog',
            name='current_status',
            field=models.IntegerField(choices=[(0, 'New'), (1, 'Processing'), (2, 'Fulfilled'), (3, 'Shipped'), (4, 'Delivered'), (5, 'Cancelled'), (6, 'Returned'), (7, 'Completed')], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderstatuslog',
            name='previous_status',
            field=models.IntegerField(choices=[(0, 'New'), (1, 'Processing'), (2, 'Fulfilled'), (3, 'Shipped'), (4, 'Delivered'), (5, 'Cancelled'), (6, 'Returned'), (7, 'Completed')], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderstatuslog',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'New'), (1, 'Processing'), (2, 'Fulfilled'), (3, 'Shipped'), (4, 'Delivered'), (5, 'Cancelled'), (6, 'Returned'), (7, 'Completed')], default=0),
        ),
    ]
