# Generated by Django 2.2.5 on 2019-10-10 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgroTech', '0006_consumersign'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating', models.CharField(max_length=30)),
                ('Comments', models.CharField(max_length=30)),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='agentsign',
            name='Pincode',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='consumersign',
            name='Pincode',
            field=models.IntegerField(default=None),
        ),
    ]
