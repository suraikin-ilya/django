# Generated by Django 3.2 on 2021-05-12 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=50, verbose_name='Марка автомобиля')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField(verbose_name='Стоимость аренды')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.brand')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(verbose_name='Имя')),
                ('surname', models.TextField(verbose_name='Фамилия')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('color_id', models.AutoField(primary_key=True, serialize=False)),
                ('color_name', models.TextField(verbose_name='Название цвета')),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_status', models.CharField(choices=[('v', 'Выполнен'), ('o', 'Отклонён'), ('d', 'Ожидает оплаты'), ('n', 'На рассмотрении')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('car_status', models.CharField(choices=[('z', 'Забронирована'), ('d', 'Доступна для аренды')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('transmission_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('a', 'Автомат'), ('m', 'Механика'), ('r', 'Роботизированная'), ('v', 'Вариативная')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('photo_id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.TextField(verbose_name='url')),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.car')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.car')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.client')),
                ('order_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.orderstatus')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.TextField(verbose_name='Телефон')),
                ('e_mail', models.TextField(verbose_name='e-mail')),
                ('address', models.TextField(verbose_name='Адресс')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.client')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='car_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.status'),
        ),
        migrations.AddField(
            model_name='car',
            name='color_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.color'),
        ),
        migrations.AddField(
            model_name='car',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.transmission'),
        ),
    ]