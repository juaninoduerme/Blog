# Generated by Django 4.0.3 on 2022-04-13 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0003_video_alter_pelicula_genero_alter_serie_genero_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='idPelicula',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='serie',
            name='idSerie',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='video',
            name='idVideo',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
