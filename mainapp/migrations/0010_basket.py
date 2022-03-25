# Generated by Django 4.0.3 on 2022-03-21 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0009_alter_items_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ManyToManyField(blank=True, related_name='PRODUCTS', to='mainapp.items')),
            ],
            options={
                'verbose_name': 'Basket',
                'verbose_name_plural': 'Baskets',
                'ordering': ['order'],
            },
        ),
    ]
