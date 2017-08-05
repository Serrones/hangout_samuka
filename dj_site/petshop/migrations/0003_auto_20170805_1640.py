# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petshop', '0002_dono'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=100)),
                ('re', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='dono',
            name='tel',
            field=models.CharField(max_length=13),
        ),
    ]
