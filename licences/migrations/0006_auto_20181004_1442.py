# Generated by Django 2.1.1 on 2018-10-04 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licences', '0005_auto_20181001_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agerange',
            name='end_age',
            field=models.IntegerField(verbose_name='Edad final'),
        ),
        migrations.AlterField(
            model_name='agerange',
            name='start_age',
            field=models.IntegerField(verbose_name='Edad inicial'),
        ),
    ]
