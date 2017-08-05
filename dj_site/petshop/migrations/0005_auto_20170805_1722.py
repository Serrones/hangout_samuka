# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petshop', '0004_auto_20170805_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('atendido', models.DateField(auto_now_add=True)),
                ('animal', models.ForeignKey(default=1, to='petshop.Animal')),
            ],
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='resp',
        ),
        migrations.AddField(
            model_name='atendimento',
            name='func',
            field=models.ForeignKey(default=1, to='petshop.Funcionario'),
        ),
    ]
