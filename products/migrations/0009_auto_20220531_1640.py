# Generated by Django 3.2 on 2022-05-31 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_inventory_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.color'),
        ),
    ]
