# Generated by Django 4.2.14 on 2024-11-12 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='duration2',
            new_name='duration_2',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='price2',
            new_name='price_2',
        ),
    ]
