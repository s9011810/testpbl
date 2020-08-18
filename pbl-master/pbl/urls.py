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
from login import views
from pbltest.views import cardind,  card_list, card_list_view, CreateView, delete_card, UploadView, post_card, \
    change_card, card_manage, screen_shot, check_card, preview_card, post_card1, preview_card1, change_card1, uploadcard
from easy_pdf.views import PDFTemplateView
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('card/<int:pk>', cardind, name='card'),
    path('upload_card/', uploadcard, name='upload_card'),
    path('class/card_list/<int:pk>', delete_card, name='class_delete_card'),
    path('checkcard/', card_list_view, name='check_card'),
    path('createcard/<int:pk>', post_card, name='createcard'),
    path('changecard/<int:pk>', change_card, name='change_card'),
    path('card_manage', card_manage, name='card_manage'),
    path('hello', PDFTemplateView.as_view(template_name='hello.html'), name='pdf'),
    path('screen_shot', screen_shot, name='screen_shot'),
    path('c_card/', check_card),
    path('createcardrow/<int:pk>', post_card1, name='createcardrow'), #橫式表單
    path('preview_card/<int:pk>', preview_card, name='preview_card'),
    path('preview_card1/<int:pk>', preview_card1, name='preview_card1'),
    path('changecard1/<int:pk>', change_card1, name='change_card1'),
    path('createclass', views.create_class, name='create_class'),
    path('activate_view/<int:pk>', views.view_activate, name='view_activate'),
    path('creatactivate', views.create_activate, name='create_activate'),
    path('creategroup/<int:pk>', views.create_group, name='create_group'),
    path('group_view/<int:pk>', views.view_group, name='view_group'),
    path('check_group/', views.check_group, name='check_group'),
    path('delete_group/<int:pk>', views.delete_group, name='delete_group'),
    path('edit_group/<int:pk>', views.edit_group, name='edit_group')
 ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
