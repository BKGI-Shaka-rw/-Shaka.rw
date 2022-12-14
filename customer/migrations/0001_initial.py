# Generated by Django 3.0.5 on 2022-12-05 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detailsName', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professionName', models.ManyToManyField(to='customer.ProfessionDetails')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.CharField(blank=True, choices=[('Driving_License', 'Driving_License'), ('Rwandan Nationals', 'Rwandan Nationals'), ('Refugee ID', 'Refugee ID'), ('Passport', 'Passport'), ('ForeignerID', 'ForeignerID'), ('Registration Number', 'Registration Number')], max_length=255)),
                ('identificationId', models.CharField(blank=True, max_length=255)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('sex', models.CharField(blank=True, choices=[('Male', 'MALE'), ('Female', 'Female'), ('Corporate', 'Corporate')], max_length=255)),
                ('dateofbirth', models.DateField(blank=True, max_length=255)),
                ('prefered_language', models.CharField(blank=True, choices=[('KINYARWANDA', 'Kinyarwanda'), ('ENGLISH', 'English'), ('SWAHILI', 'Swahili')], max_length=255)),
                ('province', models.CharField(blank=True, max_length=255)),
                ('district', models.CharField(blank=True, max_length=255)),
                ('sector', models.CharField(blank=True, max_length=255)),
                ('cell', models.CharField(blank=True, max_length=255)),
                ('village', models.CharField(blank=True, max_length=255)),
                ('civil_status', models.CharField(blank=True, choices=[('Married', 'Married'), ('Widowed', 'Widowed'), ('Separated', 'Separated'), ('Divorced', 'Divorced'), ('Single', 'Single'), ('Not Applicable', 'Not Applicable')], max_length=255)),
                ('client_status', models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Delete', 'Delete')], max_length=255)),
                ('education', models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.PROTECT, to='customer.Education')),
                ('profession', models.ForeignKey(blank=True, max_length=255, on_delete=django.db.models.deletion.PROTECT, to='customer.Profession')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255)),
                ('mobile', models.CharField(blank=True, max_length=20)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
