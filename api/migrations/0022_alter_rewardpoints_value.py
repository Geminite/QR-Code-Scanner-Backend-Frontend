# Generated by Django 4.1.5 on 2023-02-03 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_alter_log_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewardpoints',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]