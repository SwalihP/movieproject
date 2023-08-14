"""
URL configuration for movieproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from movieapp import views
app_name='movieapp'

urlpatterns = [

    # path('',views.home,name='home'),
    path('',views.Movielistview.as_view(),name="home"),
    # path('addmovie',views.addmovie,name='addmovie'),
    path('addmovie',views.Movieaddview.as_view(),name='addmovie'),
    # path('view/<int:p>/',views.moviedetail,name='moviedetails'),
    path('view/<int:pk>/',views.Moviedetailview.as_view(),name='moviedetails'),
    # path('update/<int:p>/',views.updatemovie,name='updatemovie'),
    path('update/<int:pk>/',views.Movieupdateview.as_view(),name='updatemovie'),
    # path('delete/<int:p>/',views.deletemovie,name='deletemovie'),
    path('delete/<int:pk>/',views.Moviedeleteview.as_view(),name='deletemovie')
]
