from django.contrib import admin
from .models import FileCard, UPCard, Card, TestCard
# Register your models here.

admin.site.register(FileCard)
admin.site.register(UPCard)
admin.site.register(Card)
admin.site.register(TestCard)