# Generated by Django 2.2.3 on 2019-07-29 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Select', '0002_auto_20190729_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bran',
            name='branch',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cou',
            name='course',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sec',
            name='section',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='semes',
            name='semester',
            field=models.CharField(max_length=100),
        ),
    ]
