# Generated by Django 3.2 on 2021-05-18 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='order',
        ),
    ]