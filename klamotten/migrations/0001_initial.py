# Generated by Django 3.2.7 on 2021-10-15 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Artikel',
            fields=[
                ('Name', models.CharField(max_length=64)),
                ('Artikelnummer', models.IntegerField(primary_key=True, serialize=False)),
                ('size', models.ManyToManyField(to='klamotten.Size')),
            ],
        ),
    ]
