# Generated by Django 4.1.5 on 2023-02-06 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='stock',
            field=models.BooleanField(default=True),
        ),
    ]