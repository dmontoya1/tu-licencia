# Generated by Django 2.1.1 on 2018-10-08 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_auto_20181004_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='state',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
