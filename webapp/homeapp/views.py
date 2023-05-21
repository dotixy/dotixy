# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Drawing

def index(request):
    # display the index page with a canvas element
    return render(request, 'index.html')

def save(request):
    # save the drawing data as a base64 string in the database
    if request.method == 'POST':
        data = request.POST.get('data')
        drawing = Drawing(data=data)
        drawing.save()
        return HttpResponse('Drawing saved')
    else:
        return HttpResponse('Invalid request')

def gallery(request):
    # display the gallery page with all the saved drawings
    drawings = Drawing.objects.all()
    return render(request, 'gallery.html', {'drawings': drawings})
