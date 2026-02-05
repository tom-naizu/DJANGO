from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post_details(request,post_id):
    return HttpResponse(f"<h1>User Blog Post:{post_id}</h1>")

def user_profile(request,username):
    return HttpResponse(f"<h1>Profile of user:{username}</h1>")

# def article_of_year(request,year):
#     return HttpResponse(f"<h1>Article of the year: {year}</h1>")

# def article_detail(request,year,months):
#     return HttpResponse(f"<h1>Article from {year} - {months}</h1>")

# def article_details(request,**kwargs):
#     return HttpResponse(f"<h1>Article of the year: {kwargs['year']} - {kwargs['months']}</h1>")

def article_details(request,**kwargs):
    return HttpResponse(f"<h1>Data: {kwargs}</h1>")