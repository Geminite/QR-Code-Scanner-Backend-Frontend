# Generated by Django 4.1.5 on 2023-02-12 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_allocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='allocation',
            name='placeholder',
            field=models.CharField(default='A', max_length=1000),
        ),
    ]
