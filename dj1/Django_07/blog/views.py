from django.shortcuts import render
from datetime import datetime

# Create your views here.
def blog_details(request):
    post = {
        "title" : "My Blog Page ",
        "descriptions" : "This is the web page Of BLOG Details",
        "author" : None,
        "created_at" : datetime(2005,12,6,12,46),
        "comment_count" : 5,
        "tag" : ["Django", "Python", "Web_Development"],
    }
    
    return render(request,'blog/blog_details.html',post)
