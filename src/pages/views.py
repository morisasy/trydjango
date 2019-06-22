from django.http import HttpResponse
from django.shortcuts import render


#views
def index(request):
    return HttpResponse("Hello, world")

def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	my_context = {
	"my_text": "This is about us",
	"my_number": 1239,
	"my_list": [1313, 4231, 312, "Abc"],
	"my_html": "<h1>Hellow World</h1>"
	}
	return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
	return render(request, "social.html", {})
