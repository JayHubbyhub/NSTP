# Generated by Django 4.2 on 2023-04-14 14:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0010_alter_verification_submissiondate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification',
            name='submissionDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 14, 22, 35, 39, 925594)),
        ),
    ]
