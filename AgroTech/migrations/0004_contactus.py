# Generated by Django 2.2.5 on 2019-09-29 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgroTech', '0003_farmerregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=30)),
                ('Lname', models.CharField(max_length=30)),
                ('email1', models.EmailField(max_length=30)),
                ('textf', models.EmailField(max_length=30)),
            ],
        ),
    ]
