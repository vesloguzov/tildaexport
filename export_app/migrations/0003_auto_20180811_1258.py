# Generated by Django 2.1 on 2018-08-11 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('export_app', '0002_auto_20180811_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='static_files',
            field=models.ManyToManyField(blank=True, to='export_app.StaticFile'),
        ),
        migrations.AlterField(
            model_name='project',
            name='ProjectPages',
            field=models.ManyToManyField(blank=True, to='export_app.Page'),
        ),
        migrations.AlterField(
            model_name='project',
            name='static_files',
            field=models.ManyToManyField(blank=True, to='export_app.StaticFile'),
        ),
    ]
