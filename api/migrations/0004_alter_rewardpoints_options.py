# Generated by Django 4.1 on 2022-08-20 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_rewardpoints_options_alter_rewardpoints_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rewardpoints',
            options={'verbose_name': 'Reward Point'},
        ),
    ]