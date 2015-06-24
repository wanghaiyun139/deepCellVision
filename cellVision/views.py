from django.shortcuts import render
from django.http  import HttpResponse, HttpResponse
from .forms import CellVisionForm
# Create your views here.

def classify(request):
    if request.method == 'POST':
        form = CellVisionForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            choices = form.cleaned_data['options']
            print type(image)
            return HttpResponse('image upload success')
    else:
        form = CellVisionForm()
	context_data = {'form': form}
    return render(request, 'cellVision/classify.html', {'form': form})

def segment(request):
    if request.method == 'POST':
        form = CellVisionForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            choices = form.cleaned_data['options']
            print type(image)
            return HttpResponse('image upload success')
    else:
        form = CellVisionForm()
	context_data = {'form': form}
    return render(request, "cellVision/segment.html", {'form': form})
