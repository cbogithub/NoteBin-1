# Generated by Django 2.1.1 on 2019-03-25 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the note', max_length=200)),
                ('time_created', models.DateTimeField()),
                ('time_modified', models.DateTimeField()),
                ('note', models.TextField()),
            ],
        ),
    ]
