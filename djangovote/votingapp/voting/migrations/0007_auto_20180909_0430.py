# Generated by Django 2.0.7 on 2018-09-09 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0006_auto_20180908_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='evalu1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='evalu2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='evalu3',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='evalu4',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='speaker1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='speaker2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='speaker3',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='speaker4',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='table1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='table2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='table3',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='table4',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='table5',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='table6',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='table7',
            field=models.IntegerField(default=0),
        ),
    ]