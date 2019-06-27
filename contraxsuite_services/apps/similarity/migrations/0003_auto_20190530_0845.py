# Generated by Django 2.2 on 2019-05-30 08:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0140_auto_20190530_0845'),
        ('similarity', '0002_remove_documentsimilarityconfig_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentsimilarityconfig',
            name='date_constraint_days',
            field=models.IntegerField(blank=True, default=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='documentsimilarityconfig',
            name='date_constraint_field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='document.DocumentField'),
        ),
    ]