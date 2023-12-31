from enum import Enum

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Categories(Enum):
    FOOD = "Питание"
    LEISURE = "Досуг"
    OTHER = "Другое"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

    @classmethod
    def get_value_from_string(cls, text: str):
        for item in cls:
            if item.name == text.strip():
                return Categories(item.name)
        return Categories.OTHER.value


class Subcategories(Enum):
    MUSEUMS = "Музеи"
    CINEMAS = "Кинотеатры"
    CAFFE = "Кафе"
    SHOPPING_CENTERS = "Торгово-развлекательные центры"
    RESTAURANTS = "Рестораны"
    ACTIVE_LEISURE = "Активный отдых"
    BARS = "Бары"
    CONCERT_HALLS = "Концертные и выставочные залы"
    THEATERS = "Театры"
    OTHER = "Другое"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

    @classmethod
    def get_value_from_string(cls, text: str):
        for item in cls:
            if item.name == text.strip():
                return Subcategories(item.name)
        return Subcategories.OTHER.value


class AbstractPost(models.Model):
    title = models.CharField(_('Заголовок'), max_length=100)
    description = models.TextField(_('Описание'), max_length=400, default='', blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class EventPost(AbstractPost):

    class Meta:
        verbose_name = "Пост события"
        verbose_name_plural = "Посты событий"

    address = models.CharField(_("Адррес"), max_length=100)

    category = models.CharField(_("Категория"), max_length=100, default='')
    subcategory = models.CharField(_("Вторичная категория"), max_length=100, default='')

    phone = models.CharField(_("Номер телефона"), default='', max_length=50)
    site = models.URLField(_("Вебсайт"), blank=True, null=True)

    is_unlimited_working_time = models.BooleanField(_("Время работы неограничено"), default=True)
    working_time_start = models.DateTimeField(_("Время работы(начало)"), blank=True, null=True)
    working_time_end = models.DateTimeField("Время работы(конец)", blank=True, null=True)

    is_unlimited_event_time = models.BooleanField(_("Время проведения неограничено"), default=True)
    event_time_start = models.DateTimeField(_("Период проведения(начало)"), blank=True, null=True)
    event_time_end = models.DateTimeField(_("Период проведения(конец)"), blank=True, null=True)

    @property
    def event_time(self) -> str:
        return ""

    @property
    def working_time(self) -> str:
        return ""

    def get_absolute_url(self):
        return reverse('event_post_detail', kwargs={'pk': self.pk})




class CulturePost(AbstractPost):

    next_post = models.ForeignKey('posts.CulturePost', on_delete=models.SET_NULL, verbose_name=_("Следующий пост"), related_name='previous_post', blank=True, null=True)

    class Meta:
        verbose_name = "Исторический пост"
        verbose_name_plural = "Исторические посты"

    def get_absolute_url(self):
        return reverse('culture_post_detail', kwargs={'pk': self.pk})


