from django.db import models
from django.urls import reverse


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand = models.CharField("Марка автомобиля", max_length=50)
    description = models.TextField("Описание")

    class Meta:
        verbose_name = ("Марка авто")
        verbose_name_plural = ("Марки авто")

    def __str__(self):
        return str(self.brand)


# TYPE_CHOICE = (
#     ('a', 'Автомат'),
#     ('m', "Механика"),
#     ('r', 'Роботизированная'),
#     ('v', 'Вариативная')
# )


class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    color_name = models.CharField("Цвет", max_length=50)

    class Meta:
        verbose_name = ("Цвет")
        verbose_name_plural = ("Цвета")

    def __str__(self):
        return self.color_name


# CAR_STATUS_CHOICE = (
#     ('z', 'Забронирована'),
#     ('d', "Доступна для аренды"),
# )


class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    model = models.CharField("Модель автомобиля", max_length=50, default='car model')
    price = models.IntegerField("Стоимость аренды")
    photo_url = models.TextField("photo_url", default='photo_url')
    car_description = models.TextField("description_car", default='car description')
    color_name = models.ForeignKey(Color, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("Автомобиль")
        verbose_name_plural = ("Автомобили")

    def __str__(self):
        return str(self.brand)

    def get_absolute_url(self):
        return reverse('car', kwargs={'car_id': self.pk})


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField("Имя", max_length=100)
    surname = models.CharField("Фамилия", max_length=100)
    mail = models.CharField("e-mail", max_length=100)
    password = models.CharField("password", max_length=100)
    phone = models.CharField("phone", max_length=100)

    class Meta:
        verbose_name = ("Пользователь")
        verbose_name_plural = ("Пользователь")

    def __str__(self):
        return str(self.name + " " + self.surname)


# ORDER_STATUS_CHOICE = (
#     ('v', 'Выполнен'),
#     ('o', "Отклонён"),
#     ('d', "Ожидает оплаты"),
#     ('n', "На рассмотрении"),
# )


# class OrderStatus(models.Model):
#     order_id = models.AutoField(primary_key=True)
#     order_status = models.CharField(max_length=50)
#
#     class Meta:
#         verbose_name = ("Статус заказа")
#         verbose_name_plural = ("Статусы заказа")
#
#     def __str__(self):
#         return self.order_status


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100, default='Имя пользователя')
    user_phone = models.CharField(max_length=20, default='Телефон')
    comment = models.TextField("Комментарий", default='comment')
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    # order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, blank=True)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Заказ")
        verbose_name_plural = ("Заказы")

    # def __str__(self):
    #     return str(self.order_status)