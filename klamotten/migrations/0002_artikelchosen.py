# Generated by Django 3.2.7 on 2021-11-03 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klamotten', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtikelChosen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=64)),
                ('size', models.CharField(max_length=64)),
            ],
        ),
    ]
