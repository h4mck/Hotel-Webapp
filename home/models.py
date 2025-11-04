from django.db import models
from wagtail.admin.panels import FieldPanel

from wagtail.models import Page


class HomePage(Page):
    template = "home/home.html"

    # def get_template(self, request, *args, **kwargs):
    #     return f"home/{self.slug}.html"



class TextPage(Page):

    template = "home/text_page.html"

    description = models.TextField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Описание"
    )

    content_panels = Page.content_panels + [
        FieldPanel('description'),
    ]