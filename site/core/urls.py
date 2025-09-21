from django.urls import path
from . import views

urlpatterns = [
    # Пустая строка '' означает главную страницу сайта
    path('', views.main_page, name='main_page'),
]