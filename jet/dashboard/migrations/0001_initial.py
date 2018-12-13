# Generated by Django 2.1.1 on 2018-12-12 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDashboardModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('module', models.CharField(max_length=255, verbose_name='module')),
                ('app_label', models.CharField(blank=True, max_length=255, null=True, verbose_name='application name')),
                ('user', models.PositiveIntegerField(verbose_name='user')),
                ('column', models.PositiveIntegerField(verbose_name='column')),
                ('order', models.IntegerField(verbose_name='order')),
                ('settings', models.TextField(blank=True, default='', verbose_name='settings')),
                ('children', models.TextField(blank=True, default='', verbose_name='children')),
                ('collapsed', models.BooleanField(default=False, verbose_name='collapsed')),
            ],
            options={
                'verbose_name': 'user dashboard module',
                'verbose_name_plural': 'user dashboard modules',
                'ordering': ('column', 'order'),
            },
        ),
    ]
