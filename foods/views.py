import urllib.parse
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DeleteView, UpdateView, FormView, ListView
from django.views import generic
from django.urls import reverse, reverse_lazy
from .models import Food, Shop, Category
from .forms import FoodForm, ShopForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.


class List(ListView):
    template_name = 'list.html'
    model = Food
    paginate_by = 5

    def get_queryset(self):
        return Food.objects.order_by('-created_at')


class ShopList(ListView):
    template_name = 'shop_list.html'
    model = Shop

    def get_queryset(self):
        return Shop.objects.order_by('-id')


class Create(CreateView):
    template_name = 'create.html'
    model = Food
    form_class = FoodForm

    # success_url = reverse_lazy('list')
    def get_success_url(self):
        return reverse('food', kwargs={"pk": self.object.pk})


class ShopCreate(CreateView):
    template_name = 'shop_create.html'
    model = Shop
    form_class = ShopForm
    success_url = reverse_lazy('shop_list')


def food_func(request, pk):
    object = get_object_or_404(Food, pk=pk)
    return render(request, 'food.html', {'object': object})


class FoodUpdate(UpdateView):
    # template_name = 'update.html'
    template_name = 'create.html'
    model = Food
    form_class = FoodForm

    def get_success_url(self):
        return reverse('food', kwargs={"pk": self.object.pk})


class FoodDlete(DeleteView):
    template_name = 'delete.html'
    model = Food
    success_url = reverse_lazy('list')


def freewords(request):
    object_list = Food.objects.all()
    keyword = request.GET.get('keyword')
    if keyword:
        keywords = keyword.split()
        for keys in keywords:
            object_list = object_list.filter(
                Q(title__icontains=keys) | Q(desc__icontains=keys) | Q(shop__name__icontains=keys)
            )

        object_list = object_list.distinct()

        messages.info(request, '[ <span class="emphasis">{}</span> ]の検索結果は['.format(keyword))
        messages.success(request, '<span class="emphasis">{}</span> ]件でした'.format(len(object_list)))

    return render(request, 'list.html', {'object_list': object_list})
