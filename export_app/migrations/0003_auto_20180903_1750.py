# Generated by Django 2.1 on 2018-09-03 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('export_app', '0002_auto_20180903_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='descr',
            field=models.TextField(blank=True, max_length=16000, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='project',
            name='descr',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
