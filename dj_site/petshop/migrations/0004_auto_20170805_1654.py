# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petshop', '0003_auto_20170805_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='dono',
            field=models.ForeignKey(default=1, to='petshop.Dono'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='resp',
            field=models.ForeignKey(default=1, to='petshop.Animal'),
        ),
    ]
