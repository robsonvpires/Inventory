from django.contrib import admin

from .models import Item, Sala, Category, User

admin.site.register(Sala)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(User)

