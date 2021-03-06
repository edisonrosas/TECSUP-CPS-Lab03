# Generated by Django 3.2.7 on 2021-09-10 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('precio', models.FloatField(blank=True)),
                ('talla', models.CharField(max_length=3)),
                ('categoria', models.CharField(blank=True, max_length=8)),
                ('descripción', models.TextField(max_length=500)),
                ('stock', models.PositiveIntegerField(default=1)),
                ('imagen', models.ImageField(upload_to='products/')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('Correo', models.CharField(max_length=50)),
                ('clave', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'store_user',
            },
        ),
    ]
