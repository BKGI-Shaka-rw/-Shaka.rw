# Generated by Django 4.1.3 on 2022-12-12 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_personalprofile_user'),
        ('insurance', '0009_rename_usage_type_insured_accidentdeath_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoverIdentification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicleManufacture_year', models.CharField(blank=True, default='2022', max_length=255, null=True)),
                ('vehicleBrand', models.CharField(blank=True, default='HYUNDAI', max_length=255, null=True)),
                ('vehicleModel', models.CharField(blank=True, default='SONATA', max_length=255, null=True)),
                ('vehiclePlateNo', models.CharField(blank=True, default='RAF98D', max_length=10, null=True)),
                ('vehicle_chassisNo', models.CharField(blank=True, default='GJG86FS', max_length=255, null=True)),
                ('vehicle_seat_capacity', models.CharField(blank=True, default='5', max_length=255, null=True)),
                ('vihecleImage', models.ImageField(blank=True, max_length=70, upload_to='media/%Y/%m/%d/')),
                ('documents', models.FileField(upload_to='')),
                ('sumInsured', models.CharField(blank=True, default='00,000.00', max_length=2555, null=True)),
                ('vehicle_usage', models.ForeignKey(blank=True, max_length=255, null=True, on_delete=django.db.models.deletion.PROTECT, to='insurance.vehiclecategory')),
            ],
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_comment', models.TextField(default='Nothing', max_length=300)),
                ('asked_date', models.DateField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Primium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.CharField(default='cust26384', max_length=70)),
                ('duration', models.CharField(blank=True, choices=[('1-2-9 Months', '1-2-9 Months'), ('1-6 Months', '1-6 Months'), ('1-3 Months', '1-3 Months')], default='1-6 Months', max_length=255, null=True)),
                ('locationCover', models.CharField(blank=True, default='Rwanda', max_length=2555, null=True)),
                ('declared_value_or_sumInsured', models.PositiveIntegerField(default=0)),
                ('selectCovers', models.CharField(blank=True, choices=[('THIRD PART LIABILITY', 'Third Part Liability'), ('OWN DAMAGE', 'Own Damage'), ('THEFT', 'Theft'), ('FIRE', 'Fire'), ('OCCUPANT', 'OCCUPANT'), ('TPL+', 'Tpl+')], default='THIRD PART LIABILITY', max_length=255, null=True)),
                ('numberOfOccupation_covered', models.PositiveIntegerField(default=1)),
                ('sum_insuredPerOccupanr', models.CharField(blank=True, default='3-Million-Rwf', max_length=255, null=True)),
                ('starting_date', models.DateField(auto_now=True)),
                ('ending_date', models.DateField(auto_now=True)),
                ('status', models.CharField(blank=True, default='pending', max_length=30, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Question',
            new_name='FeedBack_customer',
        ),
        migrations.DeleteModel(
            name='InsuranceCovers',
        ),
        migrations.AddField(
            model_name='insured',
            name='customer',
            field=models.OneToOneField(blank=True, max_length=255, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Insured', to='customer.customer'),
        ),
        migrations.DeleteModel(
            name='VehicleIdentification',
        ),
    ]
