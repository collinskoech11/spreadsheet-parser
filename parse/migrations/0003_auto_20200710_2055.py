# Generated by Django 3.0.8 on 2020-07-10 19:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parse', '0002_auto_20200710_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excelupload',
            name='document',
            field=models.FileField(upload_to='user/', validators=[django.core.validators.FileExtensionValidator(['xlsx'])]),
        ),
    ]
