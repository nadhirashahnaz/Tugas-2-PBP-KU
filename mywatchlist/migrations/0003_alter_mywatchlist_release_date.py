# Generated by Django 4.1 on 2022-09-21 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0002_alter_mywatchlist_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlist',
            name='release_date',
            field=models.TextField(),
        ),
    ]
