# Generated by Django 2.1.1 on 2018-10-01 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licences', '0003_ansvranges_price'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ansvranges',
            unique_together={('licence', 'gender', 'age_range')},
        ),
    ]
