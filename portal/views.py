from django.shortcuts import get_object_or_404, render
from .models import Conteudo, Menu


def obter_menu():
    # Itens ativos do menu, já na ordem definida no Admin
    return Menu.objects.filter(ativo=True).select_related("conteudo")


def index(request):
    conteudo = Conteudo.objects.filter(slug="inicio", ativo=True).first()
    return render(request, "portal/conteudo.html", {
        "menu": obter_menu(),
        "conteudo": conteudo,
    })


def conteudo(request, slug):
    item = get_object_or_404(Conteudo, slug=slug, ativo=True)
    return render(request, "portal/conteudo.html", {
        "menu": obter_menu(),
        "conteudo": item,
    })
