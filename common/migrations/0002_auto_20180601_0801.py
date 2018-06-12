# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-01 08:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='triggercondition',
            name='sendee',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='告警接收人'),
        ),
        migrations.AddField(
            model_name='triggercondition',
            name='trigger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Trigger', verbose_name='Trigger'),
        ),
        migrations.AddField(
            model_name='trigger',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Host', verbose_name='主机'),
        ),
        migrations.AddField(
            model_name='trigger',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Items', verbose_name='指标'),
        ),
        migrations.AddField(
            model_name='template',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='template',
            name='item',
            field=models.ManyToManyField(to='common.Items', verbose_name='指标'),
        ),
        migrations.AddField(
            model_name='hostgroup',
            name='template',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='common.Template', verbose_name='绑定模版'),
        ),
        migrations.AddField(
            model_name='host',
            name='hostgroups',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='common.HostGroup', verbose_name='主机组'),
        ),
        migrations.AddField(
            model_name='alarmevent',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Host', verbose_name='告警主机'),
        ),
        migrations.AddField(
            model_name='alarmevent',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Items', verbose_name='告警指标'),
        ),
    ]
