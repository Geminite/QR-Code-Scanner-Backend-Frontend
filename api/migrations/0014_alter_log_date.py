# Generated by Django 4.1 on 2022-12-04 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_log_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateTimeField(blank=True, default='13:53:03'),
        ),
    ]
