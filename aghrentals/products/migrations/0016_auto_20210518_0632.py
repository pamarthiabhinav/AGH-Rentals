# Generated by Django 3.2 on 2021-05-18 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20210516_1715'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='staus',
            new_name='status',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='None'),
            preserve_default=False,
        ),
    ]
