# Generated by Django 4.1 on 2022-08-20 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rewardpoints_name_rewardpoints_value'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rewardpoints',
            options={'verbose_name': 'Reward Points'},
        ),
        migrations.AlterModelTable(
            name='rewardpoints',
            table='state',
        ),
    ]
