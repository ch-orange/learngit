# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20150612_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='message',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
