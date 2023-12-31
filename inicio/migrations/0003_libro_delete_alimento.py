# Generated by Django 4.2.5 on 2023-10-20 00:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_alimento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=30)),
                ('frase', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Alimento',
        ),
    ]
