# Generated by Django 3.1 on 2020-10-09 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0005_dailyresult_ispinned'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyresult',
            name='description',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
