from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'core/home.html')


@login_required(login_url='accounts:login')
def user_lists(request):
    obj = UserList.objects.filter(Creater=request.user)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = UserCreationForm

    context = {
        'obj': obj,
        'form': form,
    }

    return render(request, 'core/user_lists.html', context)
