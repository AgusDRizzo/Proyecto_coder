# Generated by Django 4.2.5 on 2023-10-20 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infoextra',
            old_name='USER',
            new_name='user',
        ),
    ]
