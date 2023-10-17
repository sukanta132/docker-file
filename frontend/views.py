from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    sukanta = "Hello world"
    context = {
        'variable': sukanta
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')




