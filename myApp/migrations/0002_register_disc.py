# Generated by Django 5.0.3 on 2024-05-02 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='disc',
            field=models.TextField(default='cool'),
        ),
    ]
