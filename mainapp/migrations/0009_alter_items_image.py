# Generated by Django 4.0.3 on 2022-03-17 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_items_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/upload'),
        ),
    ]
