import urllib

from django.contrib import messages
from django.shortcuts import render, redirect
from .CustomAuthentication import MyCustomAuth
from .keitario_requests import keitario_get_statistic


def sign_in_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = MyCustomAuth.authenticate(request, username=username, password=password)
        if user is not None:
            return redirect('home/')
        else:
            messages.success(request, "there was an error logging in, try again..")
            return render(request, 'sign_in.html', {})
    else:
        return render(request, 'sign_in.html', {})


def home_view(request):
    if request.method == "POST":
        url = request.POST["url"]
        token = request.POST["token"]
        date_from = request.POST["date_from"]
        date_to = request.POST["date_to"]
        response = keitario_get_statistic(url, date_from, date_to, token)
        if response['statusCode'] == 200:
            return render(request, 'home.html', response)
        else:
            messages.success(request, "There was an error in your request, try again..")
            return render(request, 'home.html', {})
    else:
        return render(request, 'home.html', {})

