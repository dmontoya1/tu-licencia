# Generated by Django 2.1.1 on 2018-12-12 21:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIKey',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('key', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'verbose_name': 'Llave de API',
                'verbose_name_plural': 'Llaves de API',
                'ordering': ['-created'],
            },
        ),
    ]
