# Generated by Django 4.2.14 on 2024-11-13 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='info_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='info_text',
            field=models.TextField(max_length=500),
        ),
    ]
