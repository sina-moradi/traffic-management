# Generated by Django 4.2.18 on 2025-02-05 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_road_positioning'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='type',
            field=models.CharField(choices=[('s', 'small'), ('b', 'big')], default='s'),
        ),
    ]
