from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm, AutoForm
from django.db.models import F
import serial


ser = serial.Serial('COM7', 115200)

# Create your views here.

def index(request):
    data = Articles.objects.order_by('-vol')[:10]
    return render(request, 'main/index.html', {'data': data})

def reg(request):
    return render(request, 'main/reg.html')

def auto(request):
    name = ''

    form = AutoForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")

    if 'submit' in request.POST:
        new_serial_line = ser.read(size=2)
        data = int(new_serial_line)

        Articles.objects.filter(name=name).update(vol=F("vol") + float(data))
        Articles.objects.filter(name=name).update(non=F("non") + float(100 - data))

    submitbutton = request.POST.get("submit")
    context = {'form': form, 'name': name,
                'submitbutton': submitbutton,
             }

    return render(request, 'main/auto.html', context)
    # else:
    #     return redirect('top')


def about(request):
    return render(request, 'main/about.html')
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('top')
        else:
            error = 'Форма заполнена неверно'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)