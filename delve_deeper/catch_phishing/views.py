from django.http import HttpResponse

def index(request):
    return HttpResponse("Esto es una prueba")
