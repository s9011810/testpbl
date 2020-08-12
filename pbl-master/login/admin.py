from django.contrib import admin
from .models import User, Group, CreateActivate, CreateClass
# Register your models here.


admin.site.register(User),
admin.site.register(Group),
admin.site.register(CreateActivate),
admin.site.register(CreateClass),
