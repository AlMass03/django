from django.contrib import admin
from .models import User, Container, Rental, SibTransLog, Notification  # Все модели

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role', 'created_at')  # Какие поля отображаются в списке
    search_fields = ('name', 'email')  # Поля для поиска

admin.site.register(User)
admin.site.register(Container)
admin.site.register(Rental)
admin.site.register(SibTransLog)
admin.site.register(Notification)