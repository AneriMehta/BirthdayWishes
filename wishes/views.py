from django.shortcuts import render, get_object_or_404
from .models import Wish
# Create your views here.
def card(request, pk):
    card = get_object_or_404(Wish, pk=pk)
    return render(request, 'wishes/card.html', {'card':card})

def welcome(request):
    return render(request, 'wishes/welcome.html', {})

def cards(request):
    cards = Wish.objects.all()
    return render(request, 'wishes/cards.html', {'cards':cards})
