from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.utils import timezone
from datetime import datetime
from django.http import JsonResponse
from django.core import serializers
import json
from .models import *
from .forms import *

from .helper import get_ltp_data


# Create your views here.
def home(request):
    obj = Stock.objects.all()
    trans = Transaction.objects.filter(User=request.user)

    watch = WatchList.objects.filter(User=request.user)
    token_list = []

    for w in watch:
        token_list.append(w.Stocktoken)

    watch_stock = Stock.objects.filter(token__in=token_list)

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.User = request.user
            inst.Date = datetime.now(tz=timezone.utc)
            inst.save()
    else:
        form = TransactionForm

    return render(request, 'core/home.html', {'stocks': obj, 'form': form, 'trans': trans, 'watch': watch_stock})


@login_required(login_url='accounts:login')
def user_lists(request):
    obj = UserList.objects.filter(Creator=request.user)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_inst = form.save(commit=False)
            user_inst.Creator = request.user
            user_inst.save()
    else:
        form = UserForm

    context = {
        'obj': obj,
        'form': form,
    }

    return render(request, 'core/user_lists.html', context)


class update_userlist(UpdateView):
    form_class = UserForm
    model = UserList
    template_name = 'core/update_user.html'
    success_url = reverse_lazy('core:user_lists')


@login_required(login_url='accounts:login')
def delete_userlist(request, pk):
    UserList.objects.get(id=pk).delete()
    return redirect('core:user_lists')


@login_required(login_url='accounts:login')
def user_buckets(request):
    obj = Bucket.objects.filter(Creator=request.user)
    if request.method == 'POST':
        form = BucketForm(request.POST)
        if form.is_valid():
            buc = form.save(commit=False)
            buc.Creator = request.user
            buc.save()
            form.save_m2m()
    else:
        form = BucketForm

    context = {
        'obj': obj,
        'form': form,
    }

    return render(request, 'core/user_buckets.html', context)


class update_bucket(UpdateView):
    form_class = BucketForm
    model = Bucket
    template_name = 'core/update_bucket.html'
    success_url = reverse_lazy('core:user_buckets')


@login_required(login_url='accounts:login')
def delete_bucket(request, pk):
    Bucket.objects.get(id=pk).delete()
    return redirect('core:user_buckets')


@login_required(login_url='accounts:login')
def watch_lists(request):
    if request.method == 'POST':
        var = request.POST.get('stock')
        stonk = Stock.objects.get(token=var)
        WatchList.objects.create(
            User=request.user,
            Stocktoken=stonk.token, Stocksymbol=stonk.symbol,
            Stockname=stonk.name, Stockexch_seg=stonk.exch_seg
        )

    obj = Stock.objects.all()
    watch = WatchList.objects.filter(User=request.user)
    token_list = []

    for w in watch:
        token_list.append(w.Stocktoken)

    watch_stock = Stock.objects.filter(token__in=token_list)

    return render(request, 'core/watch_list.html', {'obj': obj, 'watch': watch_stock})


@login_required(login_url='accounts:login')
def delete_watchlist(request, pk):
    WatchList.objects.get(id=pk).delete()
    return redirect('core:watch_list')


def get_ajax(request):
    watch = WatchList.objects.filter(User=request.user)
    token_list = []

    for w in watch:
        token_list.append(w.Stocktoken)

    watch_stock = Stock.objects.filter(token__in=token_list)

    if request.is_ajax and request.method == 'GET':
        ltp = []
        print('got the request', watch_stock)
        for w in watch_stock:
            ltp.append(get_ltp_data(w))

        # instance = serializers.serialize('json', [watch_stock, ])
        print(ltp)
        instance = json.dumps(ltp)

        return JsonResponse({'ltp': instance}, status=200)
