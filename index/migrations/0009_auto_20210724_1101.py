# Generated by Django 2.2.1 on 2021-07-24 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20210724_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='file',
            field=models.FileField(blank=True, upload_to='index/data/files/'),
        ),
    ]
