# Generated by Django 2.1.1 on 2018-09-13 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0001_initial'),
        ('companies', '0011_auto_20180913_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='TuLicencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='Dirección')),
                ('phone', models.CharField(blank=True, help_text='Opcional. Sin indicativo de área', max_length=7, null=True, verbose_name='Teléfono fijo')),
                ('cellphone', models.CharField(max_length=10, verbose_name='Celular')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.City', verbose_name='Ciudad')),
                ('express_user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuario Express')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.State', verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Punto TuLicencia',
                'verbose_name_plural': 'Puntos TuLicencia',
            },
        ),
    ]
