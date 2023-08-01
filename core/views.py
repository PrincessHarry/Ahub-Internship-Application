from django.shortcuts import render, redirect
from datetime import date
from .models import *



def index(request):
    return render(request, "index.html")
def about(request):
    staffProfile = StaffList.objects.all()
    context = { 'staffProfile': staffProfile}
    return render(request, "ahubAbout.html", context)
def gallery(request):
    gallery_items = GalleryItem.objects.all()
    return render(request, 'gallery.html', {'gallery_items': gallery_items})