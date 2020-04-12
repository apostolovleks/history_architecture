# Generated by Django 3.0.4 on 2020-04-06 20:45

import audiofield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20200406_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='brief_description',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='gallery',
        ),
        migrations.AddField(
            model_name='museums',
            name='audio_text',
            field=audiofield.fields.AudioField(blank=True, help_text='Allowed type - .mp3, .wav, .ogg', upload_to='media/audio/'),
        ),
        migrations.AddField(
            model_name='museums',
            name='full_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='museums',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Language'),
        ),
        migrations.AddField(
            model_name='museums',
            name='layers',
            field=models.ManyToManyField(blank=True, related_name='museums', to='dashboard.Layers'),
        ),
        migrations.AddField(
            model_name='museums',
            name='main_picture',
            field=models.ImageField(null=True, upload_to='media/main_pictures/'),
        ),
        migrations.AddField(
            model_name='museums',
            name='map',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Map'),
        ),
        migrations.AddField(
            model_name='museums',
            name='section',
            field=models.ManyToManyField(blank=True, related_name='museums', to='dashboard.Sections'),
        ),
        migrations.AddField(
            model_name='museums',
            name='title',
            field=models.CharField(default=1, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='museums',
            name='type',
            field=models.CharField(choices=[('monument', 'monument'), ('museum', 'museum')], default=False, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articles',
            name='full_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='main_picture',
            field=models.ImageField(null=True, upload_to='media/main_pictures/'),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/gallery/')),
                ('brief_description', models.TextField()),
                ('articles', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Articles')),
                ('museums', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Museums')),
            ],
        ),
    ]