# Generated by Django 2.0.9 on 2018-10-26 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20181026_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/images'),
        ),
    ]
