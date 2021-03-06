# Generated by Django 2.1.1 on 2019-01-23 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20181226_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='cea',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Latitud'),
        ),
        migrations.AddField(
            model_name='cea',
            name='lon',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Longitud'),
        ),
        migrations.AddField(
            model_name='crc',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Latitud'),
        ),
        migrations.AddField(
            model_name='crc',
            name='lon',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Longitud'),
        ),
        migrations.AddField(
            model_name='transitdepartment',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Latitud'),
        ),
        migrations.AddField(
            model_name='transitdepartment',
            name='lon',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Longitud'),
        ),
    ]
