from django.db import models
from datetime import date

from django.urls import reverse


class Flower(models.Model):
    """Цветы"""
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цветы"
        verbose_name_plural = "Цветы"


class Country(models.Model):

    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    name = models.ManyToManyField(Flower, verbose_name="цветок", related_name="country_flower")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("country_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"
