from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Index</h1>")


def posts(request):
    return HttpResponse("<h1>Posts</h1>")

def psots_with_slug(request, slug):
    return HttpResponse(f"<h1>Posts {slug}</h1>")
