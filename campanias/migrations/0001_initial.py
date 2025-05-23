# Generated by Django 5.2.1 on 2025-05-14 07:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaña',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vacunacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finca', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('región', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('especie', models.CharField(choices=[('bovino', 'Bovino'), ('porcino', 'Porcino')], max_length=10)),
                ('cantidad', models.PositiveIntegerField()),
                ('campaña', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacunaciones', to='campanias.campaña')),
                ('vacunador', models.ForeignKey(limit_choices_to={'rol': 'vacunador'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
