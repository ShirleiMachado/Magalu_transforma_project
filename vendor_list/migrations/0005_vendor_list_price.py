# Generated by Django 2.2.17 on 2020-11-20 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_list', '0004_vendor_list_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor_list',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=20),
        ),
    ]
