# Generated by Django 4.1.3 on 2022-11-02 08:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2022, 11, 2, 8, 23, 7, 401582, tzinfo=datetime.timezone.utc))),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('comments', models.TextField()),
                ('date', models.DateTimeField(verbose_name='date')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.personal')),
            ],
        ),
    ]
