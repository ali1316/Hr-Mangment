# Generated by Django 5.0.1 on 2024-01-28 10:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('building_number', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('employee_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HrApp.branch')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='HrApp.employee'),
        ),
    ]
