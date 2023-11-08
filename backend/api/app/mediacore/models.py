from django.db import models
from django.utils.translation import gettext_lazy as _
from posts.models import EventPost, CulturePost


class ImageFile(models.Model):
    file = models.ImageField(_("Файл"))
    culture_post = models.ForeignKey(CulturePost, on_delete=models.CASCADE, related_name='images')
    event_post = models.ForeignKey(EventPost, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return f"Файл id {self.pk} - {self.file.name}"
