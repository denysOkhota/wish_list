from django.contrib import admin

from restaurant.menu.models import Menu, Employee, Restaurant

# Register your models here.

admin.site.register(Menu)
admin.site.register(Employee)
admin.site.register(Restaurant)
