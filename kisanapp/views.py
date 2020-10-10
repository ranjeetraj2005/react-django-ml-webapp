from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Maps from each view to its own JS build file that is passed into the template
VIEW_TO_JS_SRC_MAP = {
    "index":"indexBundle.js",
    "login":"loginBundle.js"
}
for page,src in VIEW_TO_JS_SRC_MAP.items():
    VIEW_TO_JS_SRC_MAP[page] = "/static/build/{}".format(src)

# Create your views here.

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    #return render(request, "index.html")
    srcPath = VIEW_TO_JS_SRC_MAP["index"]
    return render(request, 'website/page.html',{"title":"Index", "srcPath":srcPath})

# Login Page
def login(request):
    srcPath = VIEW_TO_JS_SRC_MAP["login"]
    return render(request, 'website/page.html',{"title":"Login", "srcPath":srcPath})
	
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
