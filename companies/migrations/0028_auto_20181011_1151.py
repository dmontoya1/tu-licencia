# Generated by Django 2.1.1 on 2018-10-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0027_auto_20181011_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='cea',
            name='rating',
            field=models.FloatField(default=0, verbose_name='Calificación Promedio'),
        ),
        migrations.AddField(
            model_name='crc',
            name='rating',
            field=models.FloatField(default=0, verbose_name='Calificación Promedio'),
        ),
        migrations.AddField(
            model_name='transitdepartment',
            name='rating',
            field=models.FloatField(default=0, verbose_name='Calificación Promedio'),
        ),
    ]