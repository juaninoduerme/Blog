# Generated by Django 4.0.3 on 2022-04-12 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='sinopsis',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serie',
            name='sinopsis',
            field=models.CharField(default=11, max_length=500),
            preserve_default=False,
        ),
    ]