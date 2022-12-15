from django.shortcuts import render


def home (request):
    '''This view generates a home page '''
    return render(request, 'home/home.html')
