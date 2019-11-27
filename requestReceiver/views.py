from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
import os, json, csv
from datetime import datetime
# Create your views here
from .models import AirQuality
from RamyakProject.settings import BASE_DIR

def landing_view(request):
    Data = {}

    if request.GET.get('AQ') is not None:
        if request.GET.get('CO2') is not None:
            Data['AQ_value'] = int(request.GET.get('AQ'))
            Data['CO2_value'] = int(request.GET.get('CO2'))
            Data['Time'] = str(datetime.now().strftime('%I:%M %p'))
            first = AirQuality.objects.create(dateTime=datetime.now(), CO2=Data['CO2_value'], AQ=Data['AQ_value'])
            
            with open(os.path.join(BASE_DIR, 'static', 'reading.json'), 'w+') as fp:
                json.dump(Data, fp)

            with open(os.path.join(BASE_DIR, 'static', 'reading_log.csv'), mode='a') as breach_log:
                breachWwriter = csv.writer(breach_log, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                list_list = []
                list_list.append(Data['AQ_value'])
                list_list.append(Data['CO2_value'])
                list_list.append(str(datetime.now().strftime('%I:%M %p')))
                
                
                breachWwriter.writerow(list_list)
                
                breach_log.close()

    print(request)

    return render(request, 'index.html', {})

def clear_view(request):
    with open(os.path.join(BASE_DIR, 'static', 'reading_log.csv'), mode='w+') as breach_log:
        bwriter = csv.writer(breach_log)
        bwriter.writerow(['AQI Reading', 'CO2 Reading', 'Time of Reading'])
        breach_log.close()
    return redirect('/')