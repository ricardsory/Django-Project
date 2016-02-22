# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-11 15:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectTeam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ac_name', models.CharField(max_length=30)),
                ('ac_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eq_name', models.CharField(max_length=30)),
                ('eq_projectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjectTeam.Pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('par_projectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjectTeam.Pregunta')),
                ('par_userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjectTeam.User')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr_name', models.CharField(max_length=30)),
                ('pr_description', models.CharField(max_length=200)),
                ('pr_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjectTeam.User')),
            ],
        ),
        migrations.AddField(
            model_name='actividad',
            name='ac_projectID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjectTeam.Project'),
        ),
    ]
