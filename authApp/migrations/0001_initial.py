# Generated by Django 3.2.8 on 2021-10-22 20:56

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dep_ips',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='IPS-Departamento')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Usuario')),
                ('password', models.CharField(max_length=256, verbose_name='Clave')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Ips',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='IPS')),
            ],
        ),
        migrations.CreateModel(
            name='Pruebas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('testDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('positiveTests', models.IntegerField(default=0)),
                ('negativeTests', models.IntegerField(default=0)),
                ('indeterminateTests', models.IntegerField(default=0)),
                ('totalTests', models.IntegerField(default=0)),
                ('dep_ips', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pruebas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='dep_ips',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authApp.departamento'),
        ),
        migrations.AddField(
            model_name='dep_ips',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='dep_ips',
            name='ips',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authApp.ips'),
        ),
        migrations.AddField(
            model_name='dep_ips',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
