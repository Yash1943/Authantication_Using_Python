# Generated by Django 5.0.2 on 2024-03-29 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_rename_sport_sports'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='sports',
            new_name='Sport',
        ),
    ]