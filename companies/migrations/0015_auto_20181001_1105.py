# Generated by Django 2.1.1 on 2018-10-01 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0014_auto_20180920_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ceavehicle',
            name='cea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='companies.Cea', verbose_name='CEA'),
        ),
    ]