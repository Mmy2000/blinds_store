# Generated by Django 4.2.14 on 2024-07-16 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_alter_about_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='short_description',
            field=models.TextField(default='', max_length=1000, verbose_name='description'),
            preserve_default=False,
        ),
    ]
