# Generated by Django 3.0.5 on 2020-05-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20200421_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalmap',
            name='map_x',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='generalmap',
            name='map_y',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='map',
            name='highlight_x',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='map',
            name='highlight_y',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='route',
            name='route_x',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='route',
            name='route_y',
            field=models.FloatField(default=0),
        ),
    ]