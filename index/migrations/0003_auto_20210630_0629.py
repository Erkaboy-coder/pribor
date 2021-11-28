# Generated by Django 2.2.1 on 2021-06-30 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20210621_0531'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificate',
            options={'ordering': ['appliance_id'], 'verbose_name_plural': 'Certificates'},
        ),
        migrations.AlterField(
            model_name='appliance',
            name='origin_year',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='appliance',
            name='used_year',
            field=models.DateTimeField(blank=True),
        ),
    ]