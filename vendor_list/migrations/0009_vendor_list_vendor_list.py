# Generated by Django 2.2.17 on 2020-11-20 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendor_list', '0008_auto_20201120_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor_list',
            name='vendor_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]