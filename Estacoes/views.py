from django.shortcuts import render

# Create your views here.
def escolher_estacao(request):
    return render(request, "escolher_estacao.html")

# @roxo
def cloud(request):
    return render(request, 'cloud.html')

def low_code(request):
    return render(request, "low-code.html")


# @azul
def mkt(request):
    return render(request, "mkt.html")

def sdr(request):
    return render(request, "sdr.html")



# @verde
def get(request):
    return render(request, 'get.html')

def pmo(request):
    return render(request, 'pmo.html')

def qualidade(request):
    return render(request, 'qualidade.html')


# @laranja
def bpo(request):
    return render(request, 'bpo.html')

def esg(request):
    return render(request, 'esg.html')

def rh(request):
    return render(request, 'rh.html')
