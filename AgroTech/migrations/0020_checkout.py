# Generated by Django 2.2.5 on 2019-11-11 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgroTech', '0019_auto_20191111_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contact', models.CharField(max_length=30)),
            ],
        ),
    ]
