from . import views
from django.urls import path,re_path

urlpatterns=[
    path('',views.home,name='Home'),
    path('post/<int:post_id>/' ,views.post_details,name='Post_detail'),
    path('user/<str:username>/' ,views.user_profile,name='user_profile'),
    path('article/<int:year>/<int:months>',views.article_details,name='article-fo-year-month'),

    # re_path(r'^article/(?P<year>[0-9]{4})/$',views.article_of_year,name='article_of_year'),

]