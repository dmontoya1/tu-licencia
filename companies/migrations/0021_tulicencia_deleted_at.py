# Generated by Django 2.1.1 on 2018-10-08 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0020_auto_20181008_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='tulicencia',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]