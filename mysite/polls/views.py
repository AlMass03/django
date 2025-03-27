from django.shortcuts import render
# from django.http import HttpResponse
from .models import User, Container, Rental, SibTransLog, Notification    #подгрузил из models все классы

def dataset_view(request):
    users = User.objects.all()
    containers = Container.objects.all()
    rentals = Rental.objects.all()
    sibtranslogs = SibTransLog.objects.all()
    notifications = Notification.objects.all()

    return render(request, 'dataset.html', {      #возвращает через рендер в файл  dataset
        'users': users,
        'containers': containers,
        'rentals': rentals,
        'sibtranslogs': sibtranslogs,
        'notifications': notifications
    }) 