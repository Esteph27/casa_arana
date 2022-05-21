# Generated by Django 3.2 on 2022-05-19 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='product_dimensions',
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='product_dimensions_and_composition',
            field=models.CharField(default='size and comp', max_length=200),
        ),
    ]