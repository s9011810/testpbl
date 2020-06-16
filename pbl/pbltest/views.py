from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template
from django.views.generic import ListView, CreateView
from .models import UPCard, Card
from django.urls import reverse_lazy
from . import forms
from .forms import CardForm, CreateCardForm
# Create your views here.


def post_card(request):
    if request.method == "POST":
        card_form = forms.CreateCardForm(request.POST)
        if card_form.is_valid():
            card_form.save()
            return redirect('index')
    else:
        form = CreateCardForm()
    return render(request, "create_card.html", {'form': form})


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
    return render(request, 'card_base.html', {
        'up_cards': up_cards
    })


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
    return render(request, 'cardlist.html', {'form': form})


def check_card(request):
    up_cards = Card.objects.all()
    return render(request, 'check_card.html', {
        'up_cards': up_cards
    })


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
