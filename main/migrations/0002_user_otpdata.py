# Generated by Django 3.1.7 on 2021-05-07 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otpdata',
            field=models.IntegerField(default=0, max_length=50),
        ),
    ]
