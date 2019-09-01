from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,'home/index.html')


def index2(req):
    return render(req,'home/index2.html')
