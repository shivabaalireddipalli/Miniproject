# Generated by Django 2.2.5 on 2019-11-11 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgroTech', '0020_checkout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='Contact',
        ),
        migrations.AddField(
            model_name='checkout',
            name='ProductId',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='checkout',
            name='Productprice',
            field=models.FloatField(default=None),
        ),
    ]
