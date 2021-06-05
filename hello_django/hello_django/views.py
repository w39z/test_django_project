from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, redirect


class MainView(TemplateView):

    def get(self, request):
        return redirect('calc', a=40, b=2)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['who'] = 'World'
    #     return context


def index(request, a=0, b=0):
    return render(request, 'hello_django/index.html', context={
        'result': a + b,
    })


class SecView(TemplateView):

    template_name = "hello_django/calc.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['calc'] = ''
        return context