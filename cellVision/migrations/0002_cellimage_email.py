# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cellVision', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cellimage',
            name='email',
            field=models.EmailField(default=b'', max_length=254),
        ),
    ]
