# Generated by Django 4.2.3 on 2023-08-07 10:42

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
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('order', models.IntegerField(default=0)),
                ('point', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
