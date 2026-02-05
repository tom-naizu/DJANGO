from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Blog Home Page is here...!!!")

def about(request):
    return HttpResponse("Blog About Page is here...!!!")