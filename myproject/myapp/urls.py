from django.urls import path ,include,translate_url
from . import views 
app_name = "myapp"
urlpatterns= [
     path("index", views.index, name="index"),
     #path("404", views.404 , name="404"),
     path("contact", views.contact, name="contact"),
     
     path("About", views.About, name="About"),
   
    path('blog', views.post_list.as_view(), name='post_list'),
    path('<slug:slug>/', views.post_detail.as_view(), name='post_detail'),

     ]
