import uuid

from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.files import File
from django.core.files.storage import default_storage
from django.core.files.temp import NamedTemporaryFile
from django.db import models

# Create your models here.
from django.db.models import Sum
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from account.utils.check_in_place import create_qr_code


class UserAccount(User):
    class Meta:
        proxy = True

    @property
    def reward_points(self):
        return self.transactions.aggregate(Sum('points')).get('points__sum', 0)


class CheckInURL(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    from_date = models.DateField(_("Начало действия"))
    to_date = models.DateField(_("Конец действия"))
    qr_code = models.ImageField(_("QR код"), blank=True, upload_to='qrcodes/')
    reward_points = models.PositiveIntegerField(_("Очки вознаграждения"), default=0)
    enabled = models.BooleanField(_("Действует"), default=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    # related_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    @property
    def build_url(self):
        return 'http://192.168.1.4:8000' + reverse('check_in_place', kwargs={'id': self.id})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.qr_code: return

        file_name = str(self.id) + ".png"
        file_path = create_qr_code(self.build_url, file_name)

        with NamedTemporaryFile() as temp_file:
            with open(file_path, 'rb') as file:
                temp_file.write(file.read())

            self.qr_code.save(file_name, File(temp_file), save=True)

        default_storage.delete(file_path)


class RewardPointTransaction(models.Model):
    check_in_url = models.ForeignKey(CheckInURL, on_delete=models.SET_NULL, null=True, blank=False)
    points = models.PositiveIntegerField(_("Вознаграждение"), default=0, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="transactions", null=True, blank=True)
    date = models.DateTimeField(_("Дата создания"), auto_now_add=True, editable=False)

