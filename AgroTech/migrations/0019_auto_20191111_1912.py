# Generated by Django 2.2.5 on 2019-11-11 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgroTech', '0018_add_items_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_items',
            name='id',
        ),
        migrations.AlterField(
            model_name='add_items',
            name='ProductId',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
    ]
