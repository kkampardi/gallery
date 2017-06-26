from django.shortcuts import render

# Create your views here.

def gallery_list(request):
    return request('gallery_list.html')