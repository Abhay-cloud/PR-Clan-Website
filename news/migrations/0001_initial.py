# Generated by Django 3.1 on 2021-02-08 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('sno1', models.AutoField(primary_key=True, serialize=False)),
                ('headLine', models.CharField(max_length=500)),
            ],
        ),
    ]
