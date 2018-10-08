# Generated by Django 2.1.1 on 2018-10-08 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0023_remove_ceavehicle_deleted_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='CeaRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField(default='N/A', null=True)),
                ('stars', models.IntegerField()),
                ('cea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_cea_ratings', to='companies.Cea', verbose_name='Cea')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_cea_user_ratings', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Calificacion CEA',
                'verbose_name_plural': 'Calificaciones CEA',
            },
        ),
        migrations.CreateModel(
            name='CrcRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField(default='N/A', null=True)),
                ('stars', models.IntegerField()),
                ('crc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_crc_ratings', to='companies.Crc', verbose_name='Crc')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_crc_user_ratings', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Calificacion CRC',
                'verbose_name_plural': 'Calificaciones CRC',
            },
        ),
        migrations.CreateModel(
            name='TransitRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField(default='N/A', null=True)),
                ('stars', models.IntegerField()),
                ('transit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_transit_ratings', to='companies.TransitDepartment', verbose_name='Organismo de transporte')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_transit_user_ratings', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Calificacion Organismo de transporte',
                'verbose_name_plural': 'Calificaciones Organismo de transporte',
            },
        ),
    ]
