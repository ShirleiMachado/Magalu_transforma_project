# Generated by Django 2.2.17 on 2020-11-20 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_list', '0006_vendor_list_estoque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor_list',
            name='estoque',
            field=models.IntegerField(null=True),
        ),
    ]