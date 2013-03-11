from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.\n")

def gimme500(request):
    raise NotImplementedError

