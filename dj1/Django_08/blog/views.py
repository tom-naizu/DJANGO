from django.shortcuts import render
from datetime import datetime 


def blog_list(request):
    blogs =[
        {"title":"Django Basic","is_feautre":True,"author":"Tom Naizu"},
        {"title":"Django Advanced","is_feautre":False,"author":""},
        {"title":"Django Rest Framework","is_feautre":False,"author":"Tom"},
    ]
    
    context = {
        "blogs":blogs, 
        "today":datetime.now(),
        "html_code":"<b>Welcome to MY BLOG</b>",
    }
    return render(request,'blog/blog_list.html', context)

