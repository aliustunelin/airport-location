# Generated by Django 5.0.2 on 2024-02-21 07:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('search_text', models.CharField(max_length=100)),
                ('search_count', models.IntegerField(default=0)),
                ('code', models.CharField(max_length=3)),
                ('phone_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('search_text', models.CharField(max_length=100)),
                ('search_count', models.IntegerField(default=0)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='location.country')),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('search_text', models.CharField(max_length=100)),
                ('search_count', models.IntegerField(default=0)),
                ('code', models.CharField(max_length=3)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airports', to='location.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airports', to='location.country')),
            ],
        ),
    ]
