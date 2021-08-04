from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView

from .models import *
from .forms import *


# Create your views here.
def home(request):
    obj = Stock.objects.all()
    return render(request, 'core/home.html', {'stocks': obj})


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


def delete_userlist(request, pk):
    UserList.objects.get(id=pk).delete()
    return redirect('core:user_lists')


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

def delete_bucket(request, pk):
    Bucket.objects.get(id=pk).delete()
    return redirect('core:user_buckets')


def watch_lists(request):
    return render(request, 'core/watch_list.html')


def delete_watchlist(request, pk):
    WatchList.objects.get(id=pk).delete()
    return redirect('core:watch_list')
