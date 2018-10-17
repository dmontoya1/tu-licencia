# Generated by Django 2.1.1 on 2018-10-16 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0012_auto_20181016_1038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logdocsstatus',
            options={'verbose_name': 'Log Estado de la documentación', 'verbose_name_plural': 'Logs de estados de la documentación'},
        ),
        migrations.AlterField(
            model_name='logdocsstatus',
            name='process_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Responsable del proceso'),
        ),
    ]