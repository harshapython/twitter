# Generated by Django 2.0.9 on 2018-10-26 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/static/css/images'),
        ),
    ]
