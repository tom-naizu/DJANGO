from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Shop Home Page is here...!!!")

def product(request):
    return HttpResponse("Shop Product Page is here...!!!")