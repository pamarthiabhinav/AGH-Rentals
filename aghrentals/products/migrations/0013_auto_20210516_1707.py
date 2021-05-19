# Generated by Django 3.2 on 2021-05-16 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_company_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='category',
            field=models.CharField(choices=[('bike', 'Bike'), ('camera', 'Camera'), ('car', 'Car')], max_length=10),
        ),
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(upload_to='companies/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('bike', 'Bike'), ('camera', 'Camera'), ('car', 'Car')], max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product/'),
        ),
    ]
