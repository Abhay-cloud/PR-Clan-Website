# Generated by Django 3.1 on 2020-11-02 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('sno1', models.AutoField(primary_key=True, serialize=False)),
                ('disname', models.CharField(max_length=255)),
                ('action1', models.TextField()),
            ],
        ),
    ]
