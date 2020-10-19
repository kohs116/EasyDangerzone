# Generated by Django 3.1.2 on 2020-10-18 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('url', models.TextField()),
                ('filetype', models.CharField(max_length=10)),
                ('md5', models.TextField()),
                ('sha256', models.TextField()),
                ('signature', models.CharField(max_length=10)),
            ],
        ),
    ]
