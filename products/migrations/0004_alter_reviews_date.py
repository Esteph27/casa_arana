# Generated by Django 3.2 on 2022-05-27 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
