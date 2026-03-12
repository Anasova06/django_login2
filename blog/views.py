from django.shortcuts import render

def home(request):
    return render(request, 'home.html') 

def about(request):
    return render(request, 'about.html')
def ismim(request):
    return render(request, 'ismim.html')


def familiyam(request):
    return render(request, 'familiyam.html')

def yoshim(request):
    return render(request, 'yoshim.html')

def university(request):
    return render(request, 'university.html')
