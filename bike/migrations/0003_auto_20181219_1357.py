# Generated by Django 2.1.2 on 2018-12-19 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0002_auto_20181218_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twowheeler',
            name='Model_Info',
            field=models.FileField(upload_to=''),
        ),
    ]
