from django.contrib import admin
from django.urls import path, include
from .views import List, Create, ShopCreate, food_func, FoodUpdate, FoodDlete, freewords, ShopList

urlpatterns = [
    path('list/', List.as_view(), name='list'),
    path('shop_list/', ShopList.as_view(), name='shop_list'),
    path('create/', Create.as_view(), name='create'),
    path('shop_create/', ShopCreate.as_view(), name='shop_create'),
    path('food/<int:pk>', food_func, name='food'),
    path('update/<int:pk>', FoodUpdate.as_view(), name='update'),
    path('delete/<int:pk>', FoodDlete.as_view(), name='delete'),
    path('freewords/', freewords, name='freewords')
]
