# Generated by Django 2.2.1 on 2021-10-18 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0012_appliance_is_delete'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificate',
            options={'ordering': ['id'], 'verbose_name_plural': 'Certificates'},
        ),
    ]