# Generated by Django 2.1.1 on 2018-10-18 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('licences', '0007_auto_20181004_1502'),
        ('request', '0014_request_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestTramit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tramit_type', models.CharField(choices=[('FL', 'Primera Licencia'), ('SL', 'Segunda Licencia'), ('RN', 'Renovación'), ('RC', 'Recategorización'), ('DU', 'Duplicado')], max_length=2, verbose_name='Tipo de Trámite')),
                ('licence', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='licences.Licence', verbose_name='Licencia')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.Request', verbose_name='Trámites')),
            ],
        ),
    ]
