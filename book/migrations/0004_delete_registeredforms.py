# Generated by Django 4.0.3 on 2022-04-06 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_rename_data_registeredforms'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RegisteredForms',
        ),
    ]
