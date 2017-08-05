# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petshop', '0005_auto_20170805_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atendimento',
            old_name='atendido',
            new_name='consulta',
        ),
        migrations.RenameField(
            model_name='atendimento',
            old_name='func',
            new_name='responsavel',
        ),
    ]
