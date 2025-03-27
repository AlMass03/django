from rest_framework import viewsets
from .models import User, Container, Rental, SibTransLog, Notification
from .serializers import UserSerializer, ContainerSerializer, RentalSerializer, SibTransLogSerializer, NotificationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ContainerViewSet(viewsets.ModelViewSet):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

class SibTransLogViewSet(viewsets.ModelViewSet):
    queryset = SibTransLog.objects.all()
    serializer_class = SibTransLogSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer