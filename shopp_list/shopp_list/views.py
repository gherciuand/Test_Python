from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return HttpResponse("<h1>You are on the homepage</h1>")


# afiseaza pagina cu lista de cumparaturi

def shoplist(request):
    # colectie de date
    product_list = [
        {'name': 'Lapte', 'done': True, 'image':'/static/icons/lapte.png'},
        {'name': 'Smintina', 'done': False, 'image':'/static/icons/smintina.png'},
        {'name': 'Unt', 'done': True, 'image':'/static/icons/unt.png'},
    ]

    # render

    return render(request, "shopplist.html", {'products': product_list})
