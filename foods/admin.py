from django.contrib import admin

# Register your models here.
from .models import Food, Shop, Category

admin.site.register(Food)
admin.site.register(Shop)
admin.site.register(Category)

admin.site.site_header = 'コンテンツ管理'