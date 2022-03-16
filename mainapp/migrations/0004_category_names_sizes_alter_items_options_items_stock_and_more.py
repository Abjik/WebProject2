# Generated by Django 4.0.3 on 2022-03-11 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_items_category_items_image_items_name_items_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='CATEGORY')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Names',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='NAME')),
            ],
            options={
                'verbose_name': 'Name',
                'verbose_name_plural': 'Names',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='SIZE')),
            ],
            options={
                'verbose_name': 'Size',
                'verbose_name_plural': 'Sizes',
                'ordering': ['title'],
            },
        ),
        migrations.AlterModelOptions(
            name='items',
            options={'verbose_name': 'Item', 'verbose_name_plural': 'Items'},
        ),
        migrations.AddField(
            model_name='items',
            name='stock',
            field=models.IntegerField(default=0, verbose_name='STOCK'),
        ),
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/images'),
        ),
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='PRICE'),
        ),
        migrations.AddField(
            model_name='items',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.sizes', verbose_name='SIZE'),
        ),
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='CATEGORY'),
        ),
        migrations.AlterField(
            model_name='items',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.names', verbose_name='BRAND'),
        ),
    ]