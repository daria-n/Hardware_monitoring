from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Data
from psutil import cpu_percent, swap_memory


# Create your views here.
def index(request):
    return render(request, 'hwdata/index.html')


def json(request):
    if request.is_ajax():
        cpu_current_usage = cpu_percent()
        swap_current_usage = (100 * swap_memory().used) / swap_memory().total
        swap_current_usage = round(swap_current_usage, 2)
        Data(CPU_usage=cpu_current_usage, SWAP_usage=swap_current_usage).save()

        records = 20
        exclude_id = Data.objects.count() - records
        if exclude_id > 0:
            id_list = Data.objects.all()[exclude_id:].values_list("id", flat=True)  # only retrieve ids.
            Data.objects.exclude(pk__in=list(id_list)).delete()
        context = {'cpu usage': cpu_current_usage, 'swap usage': swap_current_usage}
        return JsonResponse(context)

    else:
        my_data = Data.objects.all()
        my_data = list(reversed(my_data))
        count = len(my_data)
        return render(request, 'hwdata/json.html', {'current_data': my_data,
                                                    'count': count})
