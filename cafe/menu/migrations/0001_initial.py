# Generated by Django 4.2.4 on 2023-08-13 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('photo', models.ImageField(upload_to='media/category_photos')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('status', models.CharField(choices=[('is_active', 'active'), ('not_active', 'inactive')], default='not_active', max_length=10)),
                ('photo', models.ImageField(upload_to='media/menu_photos')),
                ('description', models.CharField(max_length=500)),
                ('point', models.PositiveIntegerField(default=0)),
                ('category_menu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menu.category')),
            ],
        ),
    ]
