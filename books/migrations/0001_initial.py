# Generated by Django 5.0.3 on 2024-03-11 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('isbn', models.CharField(max_length=13, unique=True)),
            ],
        ),
    ]