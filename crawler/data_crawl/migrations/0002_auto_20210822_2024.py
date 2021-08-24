# Generated by Django 3.2.6 on 2021-08-22 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_crawl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_details',
            name='battery',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product_details',
            name='camera',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product_details',
            name='display',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product_details',
            name='memory',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product_details',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='product_details',
            name='processor',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
