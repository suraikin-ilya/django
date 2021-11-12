from django.contrib import admin

from .models import Brand, Color, Car, Order, User
from django.db.models.functions import Lower
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats


@admin.register(Car)
class CarAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("car_id", "brand", "model", "price", "color_name", "photo_url", "car_description")
    search_fields = ['brand', 'color_name', 'model', 'car_description']
    list_filter = ['brand', 'price']
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


# @admin.register(OrderStatus)
# class OrderStatusAdmin(admin.ModelAdmin):
#     list_display = ('order_id', "order_status")
#     list_filter = ['order_id', 'order_status']
#     pass
#
#     def get_ordering(self, request):
#         return [Lower('order_id')]


@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("order_id", "user_name", "user_phone", "comment", "car", "date")
    search_fields = ['car', "user_name", "user_phone", "comment"]
    list_filter = ['car', 'order_id', "date"]
    actions = ['restore']
    pass

    def get_ordering(self, request):
        return [Lower('order_id')]

    def restore(self, request, queryset):
        queryset.update(order_status='Отклонён')

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

    restore.short_description = 'Отклонить выбранные заказы'


@admin.register(User)
class ClientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("user_id", "name", "surname", "mail", "password", "phone")
    search_fields = ['name', 'surname', 'mail', 'phone']
    list_filter = ['name', 'surname', 'user_id']
    pass

    def get_ordering(self, request):
        return [Lower('user_id')]

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

#
# @admin.register(User)
# class ClientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = ("user_id", "name", "surname", "mail", "password", "phone")
#     search_fields = ['name', 'surname', 'mail', 'phone']
#     list_filter = ['name', 'surname', 'user_id']
#     pass
#
#     def get_ordering(self, request):
#      return [Lower('user_id')]
#
#     def get_import_formats(self):
#         formats = (
#             base_formats.XLS,
#             base_formats.XLSX,
#         )
#         return [f for f in formats if f().can_import()]
#
#     def get_export_formats(self):
#         formats = (
#             base_formats.XLS,
#             base_formats.XLSX,
#         )
#         return [f for f in formats if f().can_export()]