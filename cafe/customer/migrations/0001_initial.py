# Generated by Django 4.2.4 on 2023-08-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=14, unique=True)),
                ('order', models.IntegerField(default=0)),
                ('point', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
