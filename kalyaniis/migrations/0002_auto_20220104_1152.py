# Generated by Django 3.2.9 on 2022-01-04 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalyaniis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.CharField(default='No description provided', max_length=1000),
        ),
        migrations.AddField(
            model_name='products',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='static/images_uploaded'),
        ),
        migrations.AddField(
            model_name='products',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='static/images_uploaded'),
        ),
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='image1',
            field=models.ImageField(upload_to='static/images_uploaded'),
        ),
    ]