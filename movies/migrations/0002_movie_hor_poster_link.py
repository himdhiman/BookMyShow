# Generated by Django 2.2.3 on 2019-08-29 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Hor_Poster_Link',
            field=models.URLField(max_length=256, null='True'),
            preserve_default='True',
        ),
    ]
