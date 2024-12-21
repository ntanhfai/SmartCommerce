# Generated by Django 5.1.4 on 2024-12-21 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=3)),
                ('status', models.CharField(max_length=20)),
                ('payment_method', models.CharField(max_length=50)),
                ('reference_id', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
