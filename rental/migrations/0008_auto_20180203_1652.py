# Generated by Django 2.0.1 on 2018-02-03 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0007_auto_20180203_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='car_images/%Y/%m/%d/'),
        ),
    ]
