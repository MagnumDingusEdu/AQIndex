# Generated by Django 2.2.7 on 2019-11-27 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestReceiver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airquality',
            name='AQ',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='airquality',
            name='CO2',
            field=models.IntegerField(),
        ),
    ]
