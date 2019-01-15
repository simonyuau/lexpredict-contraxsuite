# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-01-04 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0112_auto_20181222_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentfield',
            name='display_yes_no',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='documentfield',
            name='python_coded_field',
            field=models.CharField(blank=True, choices=[('employment.employee_name', 'Employment: Employee Name'), ('employment.employer_name', 'Employment: Employer Name'), ('employment.salary', 'Employment: Salary'), ('generic.EarliestDate', 'Earliest Date'), ('generic.LatestDate', 'Latest Date'), ('generic.MaxCurrency', 'Max Currency'), ('generic.Parties', 'Parties')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='documentfielddetector',
            name='category',
            field=models.CharField(blank=True, choices=[('simple_config', 'Simple field detectors loaded and managed via "Documents: Import Simple Field Detection Config" admin task.')], db_index=True, max_length=64, null=True),
        ),
    ]