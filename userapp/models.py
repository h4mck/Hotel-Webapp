from django.contrib.auth.models import AbstractUser
from django.db import models
from wagtail.admin.panels import FieldPanel
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    passport_number = models.CharField(max_length=50, blank=True, null=True, verbose_name="Номер паспорта")
    passport_scan = models.ImageField(upload_to="passport_scans/", blank=True, null=True, verbose_name="Скан паспорта")
    phone_mob = PhoneNumberField(verbose_name='Мобильный телефон', max_length=15, blank=False, unique=True, default='')

    panels = [
        FieldPanel('username'),
        FieldPanel('passport_number'),
        FieldPanel('passport_scan'),
        FieldPanel('phone_mob'),
    ]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
