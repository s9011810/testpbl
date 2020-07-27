from django.db import models

# Create your models here.


class User(models.Model):

    gender = (
        ('guest', "學員"),
        ('teacher', "引導師"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    identify = models.CharField(max_length=123, choices=gender, default='guest')
    c_time = models.DateTimeField(auto_now_add=True)
    # group = models.ForeignKey('Group',  on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class Group(models.Model):
    group = models.CharField(max_length=128, null=True, blank=True)
    group_user = models.ManyToManyField(User, blank=True, related_name='user_user')
    activate = models.ForeignKey('CreateActivate', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.group


class CreateActivate(models.Model):
    activate_name = models.CharField(max_length=128, unique=True, null=True, blank=True)
    class_id = models.ForeignKey('CreateClass', on_delete=models.CASCADE, blank=True, null=True)
    # group = models.ManyToManyField(Group, blank=True, related_name='user_group')

    def __str__(self):
        return self.activate_name


class CreateClass(models.Model):
    class_title = models.CharField(max_length=128)

