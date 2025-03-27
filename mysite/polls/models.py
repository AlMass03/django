import datetime
from django.db import models
from django.utils import timezone  # Для работы с часовыми поясами
import uuid

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # Метод для проверки, был ли пользователь создан недавно (за последние 24 часа)
    def was_created_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)


class Container(models.Model):
    container_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Уникальный идентификатор")
    type = models.CharField(max_length=255, verbose_name="Тип контейнера")
    status = models.CharField(max_length=255, verbose_name="Статус контейнера")
    location = models.CharField(max_length=255, blank=True, null=True, verbose_name="Текущее местоположение")
    owner_id = models.UUIDField(blank=True, null=True, verbose_name="Связь с владельцем")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return f"{self.type} - {self.status}"

    # Метод для проверки, был ли контейнер создан недавно (за последние 24 часа)
    def was_created_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)


class Rental(models.Model):
    rental_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Уникальный идентификатор")
    container = models.ForeignKey('Container', on_delete=models.CASCADE, verbose_name="Контейнер")
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="Пользователь")
    start_date = models.DateTimeField(verbose_name="Дата начала аренды")
    end_date = models.DateTimeField(verbose_name="Дата окончания аренды")
    status = models.CharField(max_length=255, verbose_name="Статус аренды")
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Суточная ставка")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Rental {self.rental_id} - {self.status}"

    # Метод для проверки, была ли аренда создана недавно (за последние 24 часа)
    def was_created_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)


class SibTransLog(models.Model):
    log_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Уникальный идентификатор")
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="Пользователь", related_name="logs")
    container = models.ForeignKey('Container', on_delete=models.CASCADE, verbose_name="Контейнер", related_name="sibtranslogs")
    rental = models.ForeignKey('Rental', on_delete=models.CASCADE, verbose_name="Аренда", related_name="logs")
    action = models.CharField(max_length=255, verbose_name="Действие")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Время действия")
    details = models.TextField(blank=True, null=True, verbose_name="Дополнительная информация")

    def __str__(self):
        return f"Log {self.log_id} - {self.action} at {self.timestamp}"

    # Можно также добавить метод для проверки, был ли лог создан недавно
    def was_created_recently(self):
        return self.timestamp >= timezone.now() - datetime.timedelta(days=1)


class Notification(models.Model):
    notification_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Уникальный идентификатор")
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="Пользователь")
    rental = models.ForeignKey('Rental', on_delete=models.CASCADE, verbose_name="Аренда")
    type = models.CharField(max_length=255, verbose_name="Тип уведомления")
    notification_time = models.DateTimeField(verbose_name="Время уведомления")
    status = models.CharField(max_length=255, verbose_name="Статус уведомления")

    def __str__(self):
        return f"Notification {self.notification_id} - {self.type}"

    # Метод для проверки, было ли уведомление создано недавно
    def was_created_recently(self):
        return self.notification_time >= timezone.now() - datetime.timedelta(days=1)