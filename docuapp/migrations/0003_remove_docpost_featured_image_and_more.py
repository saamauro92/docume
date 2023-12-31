# Generated by Django 4.2.7 on 2023-11-19 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docuapp', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docpost',
            name='featured_image',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='docpost',
            name='program',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='favourites',
            field=models.ManyToManyField(blank=True, related_name='favorited_by', to='docuapp.docpost'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
