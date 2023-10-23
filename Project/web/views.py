from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .convertidor_youtube import obtener_info, descargar, descargar_file

def home(request):
    return render(request, 'home.html')

def info(request):
    url = request.GET.get('url')
    response_data = obtener_info(url)
    return JsonResponse(response_data)
def descargar_audio(request):
    url = request.GET.get('url')
    response_data = descargar(url)
    return JsonResponse(response_data)

def descargar_archivo(request):
    file = descargar_file()
    return file