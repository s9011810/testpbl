from django.db import models
from login.models import User, CreateClass, CreateActivate, Group
from django.utils import timezone
# Create your models here.

from django.db.models import CASCADE


class FileCard(models.Model):
    file_title = models.TextField()
    file_id = models.AutoField(primary_key=True)
    file_address = models.CharField(max_length=100)


class UPCard(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('login.User', on_delete=models.CASCADE, null=True, blank=True)
    cover = models.ImageField(upload_to="card/covers/", null=True, blank=True)
    class_material = models.CharField(max_length=100, null=True)
    group = models.ForeignKey('login.Group', on_delete=models.CASCADE, null=True, blank=True)
    activate = models.ForeignKey('login.CreateActivate', on_delete=models.CASCADE, null=True, blank=True)
    thumbnail = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title


class Card(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('login.User', on_delete=models.CASCADE, null=True, blank=True)
    context = models.TextField(blank=True)
    context1 = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    published_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    cover = models.ForeignKey('UPCard', on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey('login.Group', on_delete=models.CASCADE, null=True, blank=True)
    activate = models.ForeignKey('login.CreateActivate', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.cover.delete()
        super().delete(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name_plural = "Card"


class RowCard(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('login.User', on_delete=models.CASCADE, null=True, blank=True)
    context = models.TextField(blank=True)
    context1 = models.TextField(blank=True)
    context2 = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    published_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    cover = models.ForeignKey('UPCard', on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey('login.Group', on_delete=models.CASCADE, null=True, blank=True)
    activate = models.ForeignKey('login.CreateActivate', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.cover.delete()
        super().delete(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name_plural = "row_Card"


class TestCard(models.Model):
    base_img = models.TextField(null=True, blank=True)
    base_card = models.ForeignKey('Card', on_delete=models.CASCADE, null=True, blank=True)
    base_card1 = models.ForeignKey('RowCard', on_delete=models.CASCADE, null=True, blank=True)
    groups = models.ForeignKey('login.Group', on_delete=models.CASCADE, null=True, blank=True)


