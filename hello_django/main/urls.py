from django.urls import path
from . import views
from .views import SecView


urlpatterns = [
    path('', views.index, name='main'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('calc/', views.calculate, name='main_calc'),
    path('calc/<int:a>/<int:b>', views.calculate, name='calc'),
]