from django.shortcuts import render

def frontpage(request):
    return render(request, "app/forntpage.html")

def frontpage2(request):
    return render(request, "app/forntpage2.html")