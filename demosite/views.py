from django.http import HttpResponse

def index(request):
    return HttpResponse(
        "<h2><a href='https://www.google.com'>Open Google</a></h2>"
        "<h2><a href='https://www.gmail.com'>Open Gmail</a></h2>"
        "<h2><a href='https://www.youtube.com'>Open Youtube</a></h2>"
        "<h2><a href='https://www.facewook.com'>Open Facebook</a></h2>"
    )