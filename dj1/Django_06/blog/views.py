from django.shortcuts import render
from datetime import datetime

# Create your views here.
class User:
    def __init__(self,name,age):
      self.name=name
      self.age=age

def home(request):
    context = {
        "name":"Tom Naizu",
        "age":35,
        "skills":["Python","Django","React"],
        "User":User("Tom",53),
        "blog":{
            "title":"Django Template Intro",
            "content":"<b>This is the blog</b>",
            "author":{
              "name":"Naizu", 
            },
            "created_at":datetime(2026,12,6,3,45)
          },
        "empty_value":None,
       }
    return render(request,"blog/home.html",context)


