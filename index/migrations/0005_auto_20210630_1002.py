# Generated by Django 2.2.1 on 2021-06-30 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20210630_0640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appliance',
            name='certificate_number',
        ),
        migrations.AddField(
            model_name='certificate',
            name='certificate_number',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
