from django.contrib import admin

from .models import Brand, Transmission, Color, Status, Car, Photo, Client, Contact, OrderStatus, Order
from django.db.models.functions import Lower
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats


@admin.register(Car)
class CarAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("car_id", "brand", "price", "car_status", "color_name", "type")
    search_fields = ['brand', 'color_name']
    list_filter = ['car_status', 'price']
    pass

    def get_ordering(self, request):
        return [Lower('car_id')]

    def get_import_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.XLSX,
        )
        return [f for f in formats if f().can_import()]

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.XLSX,
        )
        return [f for f in formats if f().can_export()]


@admin.register(Brand)
class BrandAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('brand_id', "brand", "description")
    search_fields = ['brand', 'description']
    list_filter = ['brand_id', 'brand']
    pass

    def get_ordering(self, request):
        return [Lower('brand_id')]

    def get_import_formats(self):
        formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
        return [f for f in formats if f().can_import()]

    def get_export_formats(self):
        formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
        return [f for f in formats if f().can_export()]


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('status_id', "car_status")
    list_filter = ['status_id', 'car_status']
    pass

    def get_ordering(self, request):
        return [Lower('status_id')]


@admin.register(Transmission)
class TransmissionAdmin(admin.ModelAdmin):
    list_display = ('transmission_id', "type")
    list_filter = ['transmission_id', 'type']
    pass

    def get_ordering(self, request):
        return [Lower('transmission_id')]


@admin.register(Color)
class ColorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('color_id', "color_name")
    list_filter = ['color_id', 'color_name']
    search_fields = ['color_name']
    pass

    def get_ordering(self, request):
        return [Lower('color_id')]

    def get_import_formats(self):
        formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
        return [f for f in formats if f().can_import()]

    def get_export_formats(self):
        formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
        return [f for f in formats if f().can_export()]


@admin.register(Photo)
class PhotoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('car_id', "photo_id", "url")
    search_fields = ['photo_id']
    list_filter = ['photo_id']
    pass

    def get_ordering(self, request):
        return [Lower('photo_id')]

    def get_import_formats(self):
        formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
        return [f for f in formats if f().can_import()]

    def get_export_formats(self):
        formats = (
                  base_formats.XLS,
                  base_formats.XLSX,
            )
        return [f for f in formats if f().can_export()]


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('order_id', "order_status")
    list_filter = ['order_id', 'order_status']
    pass

    def get_ordering(self, request):
        return [Lower('order_id')]


@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("order_id", "client_id", "car", "order_status")
    search_fields = ['car']
    list_filter = ['car', 'order_id']
    pass

    def get_ordering(self, request):
        return [Lower('order_id')]

    def get_import_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.XLSX,
        )
        return [f for f in formats if f().can_import()]

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.XLSX,
        )
        return [f for f in formats if f().can_export()]


@admin.register(Client)
class ClientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("client_id", "name", "surname")
    search_fields = ['name', 'surname']
    list_filter = ['name', 'surname', 'client_id']
    pass

    def get_ordering(self, request):
        return [Lower('client_id')]

    def get_import_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.XLSX,
        )
        return [f for f in formats if f().can_import()]

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.XLSX,
        )
        return [f for f in formats if f().can_export()]


@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("client_id", "phone", "e_mail", 'address')
    search_fields = ['phone', 'e_mail', 'address']
    list_filter = ['phone', 'e_mail', 'address', 'client_id']
    pass

    def get_ordering(self, request):
        return [Lower('client_id')]

    def get_import_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.XLSX,
        )
        return [f for f in formats if f().can_import()]

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
            base_formats.XLSX,
        )
        return [f for f in formats if f().can_export()]

