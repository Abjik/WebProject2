# Generated by Django 4.0.3 on 2022-03-16 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_remove_items_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
