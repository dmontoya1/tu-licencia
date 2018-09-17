# Generated by Django 2.1.1 on 2018-09-14 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='police',
            name='name',
        ),
        migrations.AlterField(
            model_name='police',
            name='police_type',
            field=models.CharField(choices=[('TC', 'Términos y condiciones'), ('PP', 'Políticas de privacidad'), ('CO', 'Cookies')], max_length=2, unique=True, verbose_name='Tipo de Política'),
        ),
    ]
