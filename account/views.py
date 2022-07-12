from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from account.forms import SignUpForm
import requests


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username=username, password=password)
            login(request, user)

            return HttpResponseRedirect(reverse('main'))
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'account/sign_up.html', context)


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context['error']: 'username or password is wrong'
            return render(request, 'account/login.html', context)
        else:
            login(request, user)
            return HttpResponseRedirect(reverse('main'))
    else:
        return render(request, 'account/login.html', context)

# def login_view(request):
#     context = {
#
#     }
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#
#         if user is None:
#             context['error'] = 'username or password is wrong'
#             return render(request, 'accounts/login.html', context)
#         else:
#             login(request, user)
#             return HttpResponseRedirect(reverse('Store:product'))
#
#     else:
#         return render(request, 'accounts/login.html', context)

# def main_view(request):
#     find = request.GET.get('search-food')
#     user = request.user
#     url = "https://api.calorieninjas.com/v1/nutrition?query=%s" % find
#     j_data = requests.get(url, headers={'X-Api-Key': 'fAM2b/Ck6/cIQ5fdPSiQMQ==M72qK6A1YRSwSnzo'}).json()
#     calories = int(j_data['items'][0]['calories'])
#     return render(request, 'account/main.html', context={'find': find, 'user': user, 'cal': calories})
