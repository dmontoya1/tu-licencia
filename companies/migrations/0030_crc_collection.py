# Generated by Django 2.1.1 on 2018-10-16 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_auto_20181016_1006'),
        ('companies', '0029_remove_crc_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='crc',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.CompaniesAdminPrices', verbose_name='Pin sicov y recaudo banco'),
        ),
    ]
