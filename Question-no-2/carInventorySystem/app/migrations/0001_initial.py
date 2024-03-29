# Generated by Django 4.2.5 on 2024-02-02 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ElectricCar',
            fields=[
                ('car_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.car')),
                ('battery_capacity', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            bases=('app.car',),
        ),
        migrations.CreateModel(
            name='GasCar',
            fields=[
                ('car_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.car')),
                ('fuel_efficiency', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            bases=('app.car',),
        ),
    ]
