# Generated by Django 3.2 on 2021-05-14 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.IntegerField()),
                ('message', models.TextField()),
                ('status', models.CharField(choices=[('open', 'open'), ('closed', 'closed')], default='open', max_length=10)),
            ],
        ),
    ]
