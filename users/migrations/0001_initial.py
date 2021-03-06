# Generated by Django 2.1.1 on 2018-12-12 21:20

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('password', models.CharField(blank=True, max_length=128, null=True, verbose_name='Password')),
                ('user_type', models.CharField(choices=[('CEA', 'Administrador de CEA'), ('CRC', 'Administrador de CRC'), ('CLI', 'Cliente'), ('EXU', 'Usuario express')], max_length=3, verbose_name='Tipo Usuario')),
                ('document_type', models.CharField(choices=[('CC', 'C??dula de ciudadania'), ('CE', 'C??dula de extranjer??a'), ('TI', 'Tarjeta de identidad')], max_length=3, verbose_name='Tipo Documento')),
                ('document_id', models.CharField(max_length=15, verbose_name='N??mero Documento')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefono')),
                ('cellphone', models.CharField(max_length=10, verbose_name='Celular')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Direcci??n')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=2, null=True, verbose_name='G??nero')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.City', verbose_name='Ciudad')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.State', verbose_name='Departamento')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password_activation_token', models.CharField(blank=True, max_length=200, null=True, verbose_name='Token recuperar contrase??a')),
                ('is_use_token', models.BooleanField(default=False, verbose_name='Recuper?? la contrase??a?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]
