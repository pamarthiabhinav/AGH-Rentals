# Generated by Django 3.2 on 2021-05-16 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_company_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(upload_to='products/static/images/companies/'),
        ),
    ]
