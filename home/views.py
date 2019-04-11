from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Catedra
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def homepage(request):
    return render(request=request, template_name='home/home.html', context={"Catedra": Catedra.objects.all})


def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada con exito: {username}')
            login(request, user)
            messages.info(request, f'Ingresado como {username}')
            return redirect('home:homepage')
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}:{form.error_messages[msg]}')

    form = UserCreationForm
    return render(request, 'home/register.html', context={'form': form})
