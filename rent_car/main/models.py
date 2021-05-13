from django.db import models


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand = models.CharField("Марка автомобиля", max_length=50)
    models.CharField("Модель", max_length=50)
    description = models.TextField("Описание")

    class Meta:
        verbose_name = ("Модель")
        verbose_name_plural = ("Модели")

    def __str__(self):
        return str(self.brand)


# TYPE_CHOICE = (
#     ('a', 'Автомат'),
#     ('m', "Механика"),
#     ('r', 'Роботизированная'),
#     ('v', 'Вариативная')
# )


class Transmission(models.Model):
    transmission_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Трансмиссия")
        verbose_name_plural = ("Трансмиссии")

    def __str__(self):
        return self.type


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


class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    car_status = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Статус")
        verbose_name_plural = ("Статусы")

    def __str__(self):
        return self.car_status


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

    def __str__(self):
        return str(self.brand)


class Photo(models.Model):
    photo_id = models.AutoField(primary_key=True)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    url = models.TextField("url")

    class Meta:
        verbose_name = ("Фото")
        verbose_name_plural = ("Фото")

    def __str__(self):
        return str(self.car_id)


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField("Имя", max_length=100)
    surname = models.CharField("Фамилия", max_length=100)

    class Meta:
        verbose_name = ("Клиент")
        verbose_name_plural = ("Клиенты")

    def __str__(self):
        return str(self.name + " " + self.surname)


class Contact(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    phone = models.CharField("Телефон", max_length=50)
    e_mail = models.CharField("e-mail", max_length=50)
    address = models.CharField("Адрес", max_length=100)

    class Meta:
        verbose_name = ("Контакт")
        verbose_name_plural = ("Контакты")

    def __str__(self):
        return str(self.client_id)


# ORDER_STATUS_CHOICE = (
#     ('v', 'Выполнен'),
#     ('o', "Отклонён"),
#     ('d', "Ожидает оплаты"),
#     ('n', "На рассмотрении"),
# )


class OrderStatus(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_status = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Статус заказа")
        verbose_name_plural = ("Статусы заказа")

    def __str__(self):
        return self.order_status


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Заказ")
        verbose_name_plural = ("Заказы")

    def __str__(self):
        return str(self.order_status)