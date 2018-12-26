# Generated by Django 2.1.1 on 2018-12-25 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0002_auto_20181212_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='paper',
            field=models.CharField(choices=[('SEND', 'Envío'), ('PICK', 'Recoger en punto')], default='SEND', max_length=4, verbose_name='Opcion entrega papeleo'),
            preserve_default=False,
        ),
    ]
