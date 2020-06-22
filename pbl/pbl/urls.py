"""pbl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from pbltest.views import index
from login import views
from pbltest.views import cardind, upload_card, card_list, CardListView, CreateView, delete_card, UploadView, post_card, change_card, card_manage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.register),
    path('card', cardind, name='card'),
    path('upload_card/', UploadView.as_view(), name='upload_card'),
    path('class/card_list/<int:pk>', delete_card, name='class_delete_card'),
    path('checkcard', CardListView.as_view(), name='check_card'),
    path('createcard/<int:pk>', post_card, name='createcard'),
    path('changecard/<int:pk>', change_card, name = 'change_card'),
    path('card_manage', card_manage, name = 'card_manage')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
