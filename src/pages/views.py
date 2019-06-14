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
	"my_number": 1239
	}
	return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
	return render(request, "social.html", {})
