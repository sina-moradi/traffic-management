# Generated by Django 4.2.18 on 2025-02-06 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_alter_car_load_volume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Positioning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='car.car')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traffics', to='car.road')),
            ],
        ),
    ]
