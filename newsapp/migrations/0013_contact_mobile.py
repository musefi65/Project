# Generated by Django 4.2.4 on 2023-09-24 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0012_site_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='mobile',
            field=models.CharField(default='0', max_length=50),
        ),
    ]
