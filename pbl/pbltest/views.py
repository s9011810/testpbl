from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from . import forms
from .forms import CardForm, CreateCardForm
from .models import UPCard, Card, TestCard
from easy_pdf.views import PDFTemplateView


def post_card(request, pk):
    post = UPCard.objects.all()
    card = UPCard.objects.get(id=pk)
    if request.method == "POST":
        card_form = forms.CreateCardForm(request.POST)
        if card_form.is_valid():
            card_form.save()
            url = reverse('preview_card', args=[pk])
            return redirect(url)
    else:
        form = CreateCardForm()
    context = {
        'form': form,
        'pk': pk,
        'card': card,
    }
    return render(request, "create_card.html", context)


def check_create_card(request):
    cards = Card.objects.all()
    return render(request, 'create_card.html', {
        'cards': cards
    })


def index(request):
    template = get_template('index.html')
    index_html = template.render(locals())
    return HttpResponse(index_html)


def cardind(request):
    up_cards = Card.objects.all()
    textbook = UPCard.objects.all()
    context = {
        'up_cards': up_cards,
        'textbook': textbook
    }
    return render(request, 'card_base.html', context)


def card_manage(request):
    up_cards = TestCard.objects.all()
    return render(request, 'card_manage.html', {
        'up_cards': up_cards
    })


def change_card(request, pk):
    unit = Card.objects.get(id=pk)
    card_form = CreateCardForm(request.POST or None, instance = unit)
    context = {
        'card_form': card_form,
        'unit': unit,
    }
    if card_form.is_valid():
        card_form.save()
        return redirect('index')
    return render(request, 'change_card.html', context)


def upload_card(request):
    context = {}
    if request.method == 'POST':
        upload_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        context['url'] = fs.url(name)
    return render(request, 'uploadcard.html', context)


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
    request.session['lucky_number'] = 8
    return render(request, 'cardlist.html', context)


def check_card(request):
    up_cards = Card.objects.all()
    carda = UPCard.objects.all()
    context = {
        'carda': carda,
        'up_cards': up_cards
    }
    return render(request, 'check_card.html', context)


class CardListView(ListView):
    model = UPCard
    template_name = "class_check_card.html"

    context_object_name = 'up_cards'


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
    context = {
        'unit': unit
    }
    test = TestCard()
    if request.method == "POST":
        test.base_img = request.POST.get('result1')
        test.save()
    return render(request,  'final_card.html', context)