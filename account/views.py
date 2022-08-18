from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q, Sum
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from Home.models import CalorieModel
from account.forms import SignUpForm, PersonalForm
import requests

from account.models import Person


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
            context['error']= 'username or password is wrong'
            return render(request, 'account/login.html', context)
        else:
            login(request, user)
            return HttpResponseRedirect(reverse('main'))
    else:
        return render(request, 'account/login.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def personal_view(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():

            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            if sex == 'XY':
                bmr = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)  # bmr men
            else:
                bmr = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)  # bmr woman
            Person.objects.update_or_create(user=request.user,
                                            defaults={'height': height, 'weight': weight, 'age': age,
                                                      'sex': sex, 'bmr': bmr})  # uniq user
            messages.success(request, 'saved!')
            # Person.bmr_computing(request)

        else:
            messages.error(request, 'false information')
    else:
        form = PersonalForm()
    today = datetime.today()
    try:
        person = Person.objects.get(user=request.user)
    except:
        person = None
    sum_calorie = CalorieModel.objects.filter(Q(user=request.user) & Q(date=today)).aggregate(
        Sum('calorie'))  # sum calorie in day
    sum_cal = sum_calorie['calorie__sum']
    context = {'form': form, 'person': person, 'sum_cal': sum_cal}
    return render(request, 'account/personal.html', context)


def edit_view(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():

            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            if sex == 'XY':
                bmr = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)  # bmr men
            else:
                bmr = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)  # bmr woman
            Person.objects.update_or_create(user=request.user,
                                            defaults={'height': height, 'weight': weight, 'age': age,
                                                      'sex': sex, 'bmr': bmr})  # uniq user
            return HttpResponseRedirect(reverse('personal'))

        else:
            messages.error(request, 'false information')
    else:
        form = PersonalForm()
    return render(request, 'account/edit.html', {'form': form})
