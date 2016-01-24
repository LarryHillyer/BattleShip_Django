# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('battleship', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipYard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ships', jsonfield.fields.JSONField(null=True)),
            ],
        ),
    ]
