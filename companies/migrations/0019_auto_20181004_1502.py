# Generated by Django 2.1.1 on 2018-10-04 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0018_transitdepartment_runt_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crc',
            name='price',
            field=models.IntegerField(help_text='Precio del servicio para una sola licencia', verbose_name='Precio del servicio'),
        ),
        migrations.AlterField(
            model_name='crc',
            name='price_double',
            field=models.IntegerField(help_text='Precio del servicio para 2 licencias', verbose_name='Precio del servicio doble'),
        ),
    ]
