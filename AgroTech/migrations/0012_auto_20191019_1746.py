# Generated by Django 2.2.5 on 2019-10-19 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgroTech', '0011_auto_20191014_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailf', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='CropRegister',
        ),
        migrations.DeleteModel(
            name='FarmerRegister',
        ),
    ]
