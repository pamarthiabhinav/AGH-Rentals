# Generated by Django 3.2 on 2021-05-16 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_company_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(upload_to='products/static/images/companies/<django.db.models.fields.CharField>/'),
        ),
    ]
