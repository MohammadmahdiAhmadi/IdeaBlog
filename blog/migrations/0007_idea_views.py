# Generated by Django 3.1.3 on 2021-02-06 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
