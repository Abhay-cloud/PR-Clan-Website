# Generated by Django 3.1 on 2020-09-30 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DailyResults',
            new_name='DailyResult',
        ),
    ]
