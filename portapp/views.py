from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def projects(request):
    
    return render(request, 'projects.html')

def about(request):
    
    return render(request, 'about.html')

def contact(request):
    
    return render(request, 'contact.html')

def creative_works(request):
    
    return render(request, 'creative-works.html')