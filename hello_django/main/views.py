from django.shortcuts import render
from .models import Task, History
from .forms import TaskForm
from django.views.generic.base import TemplateView

# Create your views here.
from django.shortcuts import render, redirect


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', context={
        'who': 'user',
        'tasks': tasks
    })


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'form is incorrect'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def calculate(request, a=0, b=0):
    value = a + b
    if value != 0:
        History(value=value).save()

    calc = History.objects.order_by('-id')[:10]
    return render(request, 'main/calculation.html', context={
        'result': value,
        'calc': calc,
    })


class SecView(TemplateView):

    template_name = "main/calc.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['calc'] = ''
        return context
