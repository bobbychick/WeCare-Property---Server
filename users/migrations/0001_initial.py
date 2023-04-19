# Generated by Django 4.0.5 on 2023-03-28 12:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUserModel',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('userId', models.CharField(default=uuid.uuid4, max_length=50, primary_key=True, serialize=False)),
                ('username', models.CharField(default=False, max_length=20, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('role', models.CharField(blank=True, choices=[('owner', 'owner'), ('company_admin', 'company_admin'), ('user', 'user')], max_length=13, null=True)),
                ('is_company_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Custom User',
            },
        ),
    ]
