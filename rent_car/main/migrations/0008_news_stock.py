# Generated by Django 3.2 on 2021-11-12 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20211112_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.AutoField(primary_key=True, serialize=False)),
                ('news_title', models.CharField(default='Заголовок', max_length=200)),
                ('news_photo_url', models.CharField(default='url', max_length=200)),
                ('news_text', models.TextField(default='news_text', verbose_name='Текст новости')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('stock_id', models.AutoField(primary_key=True, serialize=False)),
                ('stock_title', models.CharField(default='Заголовок акции', max_length=200)),
                ('stock_photo_url', models.CharField(default='url', max_length=200)),
                ('stock_text', models.TextField(default='stock_text', verbose_name='Текст акции')),
            ],
            options={
                'verbose_name': 'Акция',
                'verbose_name_plural': 'Акции',
            },
        ),
    ]