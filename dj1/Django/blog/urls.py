from . import views
from django.urls import path

urlpatterns = [
    # path('admin/', views.admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]