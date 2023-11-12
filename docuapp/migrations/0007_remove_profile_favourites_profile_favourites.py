# Generated by Django 4.2.7 on 2023-11-12 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docuapp', '0006_profile_favourites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='favourites',
        ),
        migrations.AddField(
            model_name='profile',
            name='favourites',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='docuapp.docpost'),
        ),
    ]