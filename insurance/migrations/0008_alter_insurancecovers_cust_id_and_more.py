# Generated by Django 4.1.3 on 2022-12-12 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0007_remove_vehicleidentification_cust_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancecovers',
            name='cust_id',
            field=models.CharField(default='cust71047', max_length=70),
        ),
        migrations.AlterField(
            model_name='insurancecovers',
            name='duration',
            field=models.CharField(blank=True, choices=[('1-2-9 Months', '1-2-9 Months'), ('3-9 Months', '1-2-9 Months'), ('6-6 Months', '1-2-9 Months')], default='1-6 Months', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='insurancecovers',
            name='sum_insuredPerOccupanr',
            field=models.CharField(blank=True, default='3-Million-Rwf', max_length=255, null=True),
        ),
    ]
