from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'index.html')


def contato(request):
    return render(request, 'contato.html')

def sobre(request):
    return render(request, 'sobre.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')