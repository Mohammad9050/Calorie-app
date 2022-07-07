from django.shortcuts import render
import requests
from datetime import datetime, timedelta
# Create your views here.
from Home.forms import AddForm
from Home.models import CalorieModel
from django.db.models import Sum, Q

def main_view(request):
    user = request.user
    today = datetime.now()
    context = {'user': user, 'today': today}
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            try:
                name = form.cleaned_data['name']
                url = "https://api.calorieninjas.com/v1/nutrition?query=%s" % name
                j_data = requests.get(url, headers={'X-Api-Key': 'fAM2b/Ck6/cIQ5fdPSiQMQ==M72qK6A1YRSwSnzo'}).json()
                calories = int(j_data['items'][0]['calories'])
                context['cal'] = calories
                context['name'] = name
                try:

                    obj = CalorieModel.objects.get(user=request.user, name=name, date=today)
                    obj.count += 1
                    obj.calorie += calories
                    obj.save()
                except:
                    CalorieModel.objects.create(user=request.user, name=name, calorie=calories)
            except:
                context['error'] = 'Item not found'

    else:
        form = AddForm()
    for i in range(7):
        week_day = today - timedelta(days=i)
        context[f'day{i}'] = CalorieModel.objects.filter(date=week_day)
        sum_calorie = CalorieModel.objects.filter(Q(user=request.user) & Q(date=week_day)).aggregate(Sum('calorie'))
        sum_cal = sum_calorie['calorie__sum']
        context[f'cal{i}'] = sum_cal
    context['form'] = form
    return render(request, 'Home/main.html', context)
