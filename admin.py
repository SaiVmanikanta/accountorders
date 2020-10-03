from django.contrib import admin
from account.models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'date_created']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'product', 'date_created', 'status']

class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product)
admin.site.register(Tag, TagAdmin)
admin.site.register(Order, OrderAdmin)
