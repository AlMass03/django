from django.contrib import admin
from django.urls import path, include
from polls.views import dataset_view  #  представление для dataset

urlpatterns = [
    path('admin/', admin.site.urls),  # Админ-панель
    path('', include('polls.urls')),  # Подключаем маршруты из polls, включая API
    path('dataset/', dataset_view, name='dataset_view'),  # HTML-шаблон с данными
]