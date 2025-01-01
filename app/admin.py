from django.contrib import admin
from .models import Client, Order, Photo, PrintOption, Payment

admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Photo)
admin.site.register(PrintOption)
admin.site.register(Payment)
