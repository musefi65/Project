# Generated by Django 4.2.4 on 2023-09-21 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0005_news_keyword_alter_news_catgory_alter_news_dtm_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='txt',
        ),
        migrations.AddField(
            model_name='news',
            name='pic1',
            field=models.TextField(default=' ', verbose_name='عکس یک '),
        ),
        migrations.AddField(
            model_name='news',
            name='pic2',
            field=models.TextField(default=' ', verbose_name='عکس دو'),
        ),
        migrations.AddField(
            model_name='news',
            name='pic3',
            field=models.TextField(default=' ', verbose_name='عکس سه'),
        ),
        migrations.AddField(
            model_name='news',
            name='pic4',
            field=models.TextField(default=' ', verbose_name='عکس چهار'),
        ),
        migrations.AddField(
            model_name='news',
            name='pic5',
            field=models.TextField(default=' ', verbose_name='عکس پنج'),
        ),
        migrations.AddField(
            model_name='news',
            name='titr1',
            field=models.TextField(default=' ', verbose_name='تیتر یـک '),
        ),
        migrations.AddField(
            model_name='news',
            name='titr2',
            field=models.TextField(default=' ', verbose_name=' تیتر دو '),
        ),
        migrations.AddField(
            model_name='news',
            name='titr3',
            field=models.TextField(default=' ', verbose_name='تیتر سـه '),
        ),
        migrations.AddField(
            model_name='news',
            name='txt1',
            field=models.TextField(default='خبر', verbose_name='متن یک خبر'),
        ),
        migrations.AddField(
            model_name='news',
            name='txt2',
            field=models.TextField(default=' ', verbose_name='متن دو خبر'),
        ),
        migrations.AddField(
            model_name='news',
            name='txt3',
            field=models.TextField(default=' ', verbose_name='متن سه خبر'),
        ),
        migrations.AddField(
            model_name='news',
            name='txt4',
            field=models.TextField(default=' ', verbose_name='متن چهار خبر'),
        ),
        migrations.AddField(
            model_name='news',
            name='txt5',
            field=models.TextField(default=' ', verbose_name='متن پنج خبر'),
        ),
        migrations.AddField(
            model_name='news',
            name='txt6',
            field=models.TextField(default=' ', verbose_name='متن شش خبر'),
        ),
        migrations.AddField(
            model_name='news',
            name='txt7',
            field=models.TextField(default=' ', verbose_name='متن هفت خبر'),
        ),
        migrations.AlterField(
            model_name='news',
            name='keyword',
            field=models.CharField(default='هفته نامه امین بختیاری   چهارمحال و بختیاری', max_length=60, verbose_name='کلمات کلیدی'),
        ),
    ]
