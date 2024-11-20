from django.shortcuts import render

def home(request):
    return render(request, 'base.html', {'title': 'Главная'})

def about(request):
    return render(request, 'about.html', {'title': 'О компании'})

def contact(request):
    return render(request, 'contact.html', {'title': 'Контакты'})
