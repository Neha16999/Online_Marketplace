# Generated by Django 2.1.2 on 2018-12-19 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0003_auto_20181219_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twowheeler',
            name='Model_Info',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='twowheeler',
            name='Model_img',
            field=models.FileField(upload_to=''),
        ),
    ]