# Generated by Django 4.2.5 on 2023-10-20 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_libro_delete_alimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
    ]
