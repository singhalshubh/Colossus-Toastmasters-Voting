# Generated by Django 2.0.7 on 2018-09-08 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0002_auto_20180908_1759'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='votes',
            new_name='votess',
        ),
    ]