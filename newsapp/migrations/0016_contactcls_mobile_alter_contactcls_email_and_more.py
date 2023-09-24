# Generated by Django 4.2.4 on 2023-09-24 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0015_contactcls_delete_contact_us_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactcls',
            name='mobile',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactcls',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contactcls',
            name='message',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='contactcls',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='contactcls',
            name='subject',
            field=models.CharField(max_length=200),
        ),
    ]
