from django.db import models


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand = models.CharField("Марка автомобиля", max_length=50)
    description = models.TextField("Описание")


TYPE_CHOICE = (
    ('a', 'Автомат'),
    ('m', "Механика"),
    ('r', 'Роботизированная'),
    ('v', 'Вариативная')
)


class Transmission(models.Model):
    transmission_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=1, choices=TYPE_CHOICE)


class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    color_name = models.TextField("Название цвета")


CAR_STATUS_CHOICE = (
    ('z', 'Забронирована'),
    ('d', "Доступна для аренды"),
)


class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    car_status = models.CharField(max_length=1, choices=CAR_STATUS_CHOICE)


class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    car_status = models.ForeignKey(Status, on_delete=models.CASCADE)
    price = models.IntegerField("Стоимость аренды")
    color_name = models.ForeignKey(Color, on_delete=models.DO_NOTHING)
    type = models.ForeignKey(Transmission, on_delete=models.DO_NOTHING)
    class Meta:
        verbose_name = ("Автомобиль")
        verbose_name_plural = ("Автомобили")


class Photo(models.Model):
    photo_id = models.AutoField(primary_key=True)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    url = models.TextField("url")


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.TextField("Имя")
    surname = models.TextField("Фамилия")


class Contact(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    phone = models.TextField("Телефон")
    e_mail = models.TextField("e-mail")
    address = models.TextField("Адресс")


ORDER_STATUS_CHOICE = (
    ('v', 'Выполнен'),
    ('o', "Отклонён"),
    ('d', "Ожидает оплаты"),
    ('n', "На рассмотрении"),
)


class OrderStatus(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_status = models.CharField(max_length=1, choices=ORDER_STATUS_CHOICE)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    class Meta:
        verbose_name = ("Заказ")
        verbose_name_plural = ("Заказы")
