# Generated by Django 4.2.3 on 2023-09-01 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('cnpj', models.CharField(max_length=255, verbose_name='CNPJ')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('phone', models.CharField(max_length=255, verbose_name='Phone')),
                ('street', models.CharField(max_length=255, verbose_name='Street')),
                ('number', models.CharField(max_length=255, verbose_name='Number')),
                ('neighborhood', models.CharField(max_length=255, verbose_name='Neighborhood')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
                ('state', models.CharField(max_length=255, verbose_name='State')),
                ('country', models.CharField(max_length=255, verbose_name='Country')),
                ('zipcode', models.CharField(max_length=255, verbose_name='Zipcode')),
            ],
        ),
    ]