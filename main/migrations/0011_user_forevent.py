# Generated by Django 3.2.4 on 2021-07-05 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='forevent',
            field=models.IntegerField(default=0),
        ),
    ]
