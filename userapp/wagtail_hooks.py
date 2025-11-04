from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import CustomUser

class CustomUserAdmin(ModelAdmin):
    model = CustomUser
    menu_label = 'Пользователи'  # Название в меню
    menu_icon = 'user'          # Иконка
    list_display = ('username', 'passport_number', 'passport_scan', 'last_name')

modeladmin_register(CustomUserAdmin)
