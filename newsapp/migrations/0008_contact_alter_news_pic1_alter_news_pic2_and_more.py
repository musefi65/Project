# Generated by Django 4.2.4 on 2023-09-22 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0007_remove_news_keyword_news_keyword1_news_keyword2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nam', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('onvan', models.CharField(max_length=150)),
                ('matn', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='pic1',
            field=models.TextField(default=' عکس خبر', verbose_name='عکس یک '),
        ),
        migrations.AlterField(
            model_name='news',
            name='pic2',
            field=models.TextField(default=' عکس خبر', verbose_name='عکس دو'),
        ),
        migrations.AlterField(
            model_name='news',
            name='pic3',
            field=models.TextField(default=' عکس خبر', verbose_name='عکس سه'),
        ),
        migrations.AlterField(
            model_name='news',
            name='pic4',
            field=models.TextField(default=' عکس خبر', verbose_name='عکس چهار'),
        ),
        migrations.AlterField(
            model_name='news',
            name='pic5',
            field=models.TextField(default=' عکس خبر', verbose_name='عکس پنج'),
        ),
        migrations.AlterField(
            model_name='news',
            name='titr1',
            field=models.TextField(default=' تیتر ', verbose_name='تیتر یـک '),
        ),
        migrations.AlterField(
            model_name='news',
            name='titr2',
            field=models.TextField(default=' تیتر ', verbose_name=' تیتر دو '),
        ),
        migrations.AlterField(
            model_name='news',
            name='titr3',
            field=models.TextField(default=' تیتر ', verbose_name='تیتر سـه '),
        ),
        migrations.AlterField(
            model_name='news',
            name='txt2',
            field=models.TextField(default=' متن خبر', verbose_name='متن دو خبر'),
        ),
        migrations.AlterField(
            model_name='news',
            name='txt3',
            field=models.TextField(default=' متن خبر', verbose_name='متن سه خبر'),
        ),
        migrations.AlterField(
            model_name='news',
            name='txt4',
            field=models.TextField(default=' متن خبر', verbose_name='متن چهار خبر'),
        ),
        migrations.AlterField(
            model_name='news',
            name='txt5',
            field=models.TextField(default=' متن خبر', verbose_name='متن پنج خبر'),
        ),
        migrations.AlterField(
            model_name='news',
            name='txt6',
            field=models.TextField(default=' متن خبر', verbose_name='متن شش خبر'),
        ),
        migrations.AlterField(
            model_name='news',
            name='txt7',
            field=models.TextField(default=' متن خبر', verbose_name='متن هفت خبر'),
        ),
    ]
