import os
import time

import cv2
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from login.models import CreateClass, CreateActivate, Group, User
from .forms import CardForm, CreateCardForm, RowCreateCardForm
from .imglib import Picture_part
from .models import UPCard, Card, TestCard, RowCard


def post_card(request, pk):
    post = UPCard.objects.all()
    card = UPCard.objects.get(id=pk)
    author = User.objects.all()
    group = Group.objects.all();
    if request.method == "POST":
        card_form = CreateCardForm(request.POST)
        if card_form.is_valid():
            final_card = card_form.save()
            url = reverse('preview_card', args=[final_card.pk])
            return redirect(url)
    else:
        card_form = CreateCardForm()
    context = {
        'form': card_form,
        'pk': pk,
        'card': card,
        'author': author,
        'group': group,
    }
    return render(request, "create_card.html", context)


def post_card1(request, pk):
    post = UPCard.objects.all()
    card = UPCard.objects.get(id=pk)

    if request.method == "POST":
        card_form = RowCreateCardForm(request.POST)
        if card_form.is_valid():
            final_card = card_form.save()
            url = reverse('preview_card1', args=[final_card.pk])
            return redirect(url)
    else:
        card_form = RowCreateCardForm()
    context = {
        'form': card_form,
        'pk': pk,
        'card': card,
    }
    return render(request, "create_card_row.html", context)


def check_create_card(request):
    cards = Card.objects.all()
    return render(request, 'create_card.html', {
        'cards': cards
    })


def index(request):
    create_class = CreateClass.objects.all()
    context = {'create_class': create_class}
    return render(request, 'index.html', context)


def cardind(request, pk):
    group = Group.objects.get(id=pk)
    group_user = group.group_user.all()
    up_cards = UPCard.objects.all()
    context = {
        'group': group,
        'group_user': group_user,
        'up_cards': up_cards,
        'pk': pk
    }
    return render(request, 'card_base.html', context)

#Todo cardmanage 轉群組需額外處理

def card_manage(request):
    up_cards = TestCard.objects.all().order_by('-groups')
    groups = Group.objects.all()
    return render(request, 'card_manage.html', {
        'up_cards': up_cards,
        'groups': groups,
    })


def change_card(request, pk):
    unit = Card.objects.get(id=pk)
    card_form = CreateCardForm(request.POST or None, instance=unit)
    context = {
        'card_form': card_form,
        'unit': unit,
    }

    print('123');
    if card_form.is_valid():
        card_form.save()
        return redirect('index')
    return render(request, 'change_card.html', context)


def change_card1(request, pk):
    unit = RowCard.objects.get(id=pk)
    card_form = RowCreateCardForm(request.POST or None, instance=unit)
    context = {
        'card_form': card_form,
        'unit': unit,
    }
    if card_form.is_valid():
        card_form.save()
        return redirect('index')
    return render(request, 'change_card1.html', context)


# 20200728
# 原urls.py 中 #path('upload_card/', UploadView.as_view(), name='upload_card'),
# 改為    path('upload_card/', views.uploadcard(), name='upload_card'),
def uploadcard(request):
    cards: UPCard
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            cards = form.save() #UPCard 的實體
            file = cards.cover.file.name
            filename = os.path.basename(file)
            #pic = Picture_part(filename)
            pic = Picture_part('media/card/covers/'+filename)

            if cards.class_material == '1': # 直式
                cards.thumbnail = 'media/card/vertical/'+filename
                cards.save()
                img = pic.vertical()
                cv2.imencode('.JPG',img)[1].tofile(cards.thumbnail)
            elif cards.class_material == '2': # 橫式
                cards.thumbnail = 'media/card/horizontal/' + filename
                cards.save()
                img = pic.horizontal()
                cv2.imencode('.JPG', img)[1].tofile(cards.thumbnail)
                #cv2.imwrite( )
            return redirect(reverse('check_card'))
    else:
        form = CardForm()
    return render(request, 'cardlist.html', {'form': form})


def card_list(request):
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('check_card')
    else:
        form = CardForm()
    context = {
        'form': form,
    }
    return render(request, 'cardlist.html', context)


def check_card(request):
    print('hello')
    print(request.user.username)
    up_cards = Card.objects.all()
    carda = UPCard.objects.all()
    context = {
        'carda': carda,
        'up_cards': up_cards
    }
    return render(request, 'check_card.html', context)


def card_list_view(request):
    up_cards = UPCard.objects.all()

    user_id = request.session['user_id']
    group = Group.objects.all()
    context = {
        'up_cards': up_cards,
        'group': group
    }
    return render(request, "class_check_card.html", context)


class UploadView(CreateView):
    model = UPCard
    form_class = CardForm
    success_url = reverse_lazy("check_card")
    template_name = "cardlist.html"


def delete_card(request, pk):
    pk = int(pk)
    if request.method == "POST":
        card = UPCard.objects.get(pk=pk)
        card.delete()
    return redirect('check_card')


def screen_shot(request):
    return render(request, 'testscreen.html')


def preview_card(request, pk):
    unit = Card.objects.get(id=pk)
    global bools
    bools = False
    context = {
        'unit': unit
    }
    test = TestCard()
    if request.method == "POST":
        test.base_img = request.POST.get('result1')
        test.base_card_id = unit.pk
        test.groups_id = unit.group.id
        test.save()
        bools = True
        if bools:
            return redirect('card_manage')
    return render(request,  'final_card.html', context)


def preview_card1(request, pk):
    unit = RowCard.objects.get(id=pk)
    context = {
        'unit': unit
    }
    test = TestCard()
    if request.method == "POST":
        test.base_img = request.POST.get('result1')
        test.base_card1_id = unit.pk
        test.groups_id = unit.group.id
        test.save()
    return render(request,  'final_card1.html', context)