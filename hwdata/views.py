from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Data
from psutil import cpu_percent, swap_memory
from django.core import serializers


# Create your views here.
def index(request):
    count = Data.objects.count()
    my_data = Data.objects.all()[count-1:]
    return render(request, 'hwdata/index.html', {'current_data': my_data})


def json(request):

    if request.is_ajax():
        cpu_current_usage = cpu_percent()
        swap_current_usage = (100 * swap_memory().used) / swap_memory().total
        swap_current_usage = round(swap_current_usage, 2)
        Data(CPU_usage=cpu_current_usage, SWAP_usage=swap_current_usage).save()
        id_list = Data.objects.all()[:500].values_list("id", flat=True)  # only retrieve ids.
        Data.objects.exclude(pk__in=list(id_list)).delete()
        context = {'cpu usage': cpu_current_usage, 'swap usage': swap_current_usage}
        return JsonResponse(context)

    else:
        my_data = Data.objects.all()
        return render(request, 'hwdata/json.html', {'current_data': my_data})
