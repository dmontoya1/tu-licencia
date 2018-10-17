# Generated by Django 2.1.1 on 2018-10-10 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_auto_20181008_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nombre Sector')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_sectors', to='manager.City', verbose_name='Ciudad')),
            ],
            options={
                'verbose_name': 'Sector',
                'verbose_name_plural': 'Sectores',
            },
        ),
    ]