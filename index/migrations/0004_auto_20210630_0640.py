# Generated by Django 2.2.1 on 2021-06-30 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20210630_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='file',
            field=models.FileField(blank=True, upload_to='index/static/files/'),
        ),
    ]
