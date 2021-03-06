# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-08 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='applicant_id',
            field=models.IntegerField(db_index=True, verbose_name='Applicant ID'),
        ),
        migrations.AlterField(
            model_name='document',
            name='cnpj_cpf',
            field=models.CharField(db_index=True, max_length=14, verbose_name='CNPJ or CPF'),
        ),
        migrations.AlterField(
            model_name='document',
            name='congressperson_id',
            field=models.IntegerField(db_index=True, verbose_name='Congressperson ID'),
        ),
        migrations.AlterField(
            model_name='document',
            name='congressperson_name',
            field=models.CharField(max_length=128, verbose_name='Congressperson name'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_id',
            field=models.IntegerField(db_index=True, verbose_name='Document ID'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_number',
            field=models.CharField(max_length=128, verbose_name='Document number'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_type',
            field=models.IntegerField(db_index=True, verbose_name='Document type'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_value',
            field=models.DecimalField(db_index=True, decimal_places=3, max_digits=10, verbose_name='Document value'),
        ),
        migrations.AlterField(
            model_name='document',
            name='leg_of_the_trip',
            field=models.CharField(max_length=128, verbose_name='Leg of the trip'),
        ),
        migrations.AlterField(
            model_name='document',
            name='month',
            field=models.IntegerField(db_index=True, verbose_name='Month'),
        ),
        migrations.AlterField(
            model_name='document',
            name='net_value',
            field=models.DecimalField(db_index=True, decimal_places=3, max_digits=10, verbose_name='Net value'),
        ),
        migrations.AlterField(
            model_name='document',
            name='party',
            field=models.CharField(db_index=True, max_length=16, verbose_name='Party'),
        ),
        migrations.AlterField(
            model_name='document',
            name='passenger',
            field=models.CharField(max_length=128, verbose_name='Passenger'),
        ),
        migrations.AlterField(
            model_name='document',
            name='reimbursement_number',
            field=models.IntegerField(db_index=True, verbose_name='Reimbursement number'),
        ),
        migrations.AlterField(
            model_name='document',
            name='reimbursement_value',
            field=models.DecimalField(db_index=True, decimal_places=3, max_digits=10, verbose_name='Reimbusrsement value'),
        ),
        migrations.AlterField(
            model_name='document',
            name='remark_value',
            field=models.DecimalField(db_index=True, decimal_places=3, max_digits=10, verbose_name='Remark value'),
        ),
        migrations.AlterField(
            model_name='document',
            name='subquota_description',
            field=models.CharField(max_length=128, verbose_name='Subquota descrition'),
        ),
        migrations.AlterField(
            model_name='document',
            name='subquota_group_description',
            field=models.CharField(max_length=128, verbose_name='Subquota group description'),
        ),
        migrations.AlterField(
            model_name='document',
            name='subquota_group_id',
            field=models.IntegerField(db_index=True, verbose_name='Subquota group ID'),
        ),
        migrations.AlterField(
            model_name='document',
            name='subquota_number',
            field=models.IntegerField(db_index=True, verbose_name='Subquote ID'),
        ),
        migrations.AlterField(
            model_name='document',
            name='term',
            field=models.IntegerField(db_index=True, verbose_name='Term'),
        ),
        migrations.AlterField(
            model_name='document',
            name='year',
            field=models.IntegerField(db_index=True, verbose_name='Year'),
        ),
    ]
