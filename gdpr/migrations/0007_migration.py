# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-02-17 13:08
from __future__ import unicode_literals

from django.db import migrations
import enumfields.fields
import gdpr.enums


class Migration(migrations.Migration):

    dependencies = [
        ('gdpr', '0006_auto_20190228_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='legalreason',
            name='state',
            field=enumfields.fields.NumEnumField(default=1, enum=gdpr.enums.LegalReasonState, verbose_name='state'),
        ),
    ]