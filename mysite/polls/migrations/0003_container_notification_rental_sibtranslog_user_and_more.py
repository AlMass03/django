# Generated by Django 4.2.20 on 2025-03-27 10:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0002_sibtransuser_delete_choice_delete_question"),
    ]

    operations = [
        migrations.CreateModel(
            name="Container",
            fields=[
                (
                    "container_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Уникальный идентификатор",
                    ),
                ),
                (
                    "type",
                    models.CharField(max_length=255, verbose_name="Тип контейнера"),
                ),
                (
                    "status",
                    models.CharField(max_length=255, verbose_name="Статус контейнера"),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Текущее местоположение",
                    ),
                ),
                (
                    "owner_id",
                    models.UUIDField(
                        blank=True, null=True, verbose_name="Связь с владельцем"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата добавления"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "notification_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Уникальный идентификатор",
                    ),
                ),
                (
                    "type",
                    models.CharField(max_length=255, verbose_name="Тип уведомления"),
                ),
                (
                    "notification_time",
                    models.DateTimeField(verbose_name="Время уведомления"),
                ),
                (
                    "status",
                    models.CharField(max_length=255, verbose_name="Статус уведомления"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Rental",
            fields=[
                (
                    "rental_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Уникальный идентификатор",
                    ),
                ),
                ("start_date", models.DateTimeField(verbose_name="Дата начала аренды")),
                (
                    "end_date",
                    models.DateTimeField(verbose_name="Дата окончания аренды"),
                ),
                (
                    "status",
                    models.CharField(max_length=255, verbose_name="Статус аренды"),
                ),
                (
                    "daily_rate",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Суточная ставка"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "container",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="polls.container",
                        verbose_name="Контейнер",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SibTransLog",
            fields=[
                (
                    "log_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Уникальный идентификатор",
                    ),
                ),
                ("action", models.CharField(max_length=255, verbose_name="Действие")),
                (
                    "timestamp",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время действия"
                    ),
                ),
                (
                    "details",
                    models.TextField(
                        blank=True, null=True, verbose_name="Дополнительная информация"
                    ),
                ),
                (
                    "container",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sibtranslogs",
                        to="polls.container",
                        verbose_name="Контейнер",
                    ),
                ),
                (
                    "rental",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="logs",
                        to="polls.rental",
                        verbose_name="Аренда",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "user_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("role", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name="SibTransUser",
        ),
        migrations.AddField(
            model_name="sibtranslog",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="logs",
                to="polls.user",
                verbose_name="Пользователь",
            ),
        ),
        migrations.AddField(
            model_name="rental",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="polls.user",
                verbose_name="Пользователь",
            ),
        ),
        migrations.AddField(
            model_name="notification",
            name="rental",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="polls.rental",
                verbose_name="Аренда",
            ),
        ),
        migrations.AddField(
            model_name="notification",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="polls.user",
                verbose_name="Пользователь",
            ),
        ),
    ]
