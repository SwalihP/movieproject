from django.shortcuts import render
from movieapp.models import Movie
from movieapp.forms import Movieform
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

# def home(request):
#     m=Movie.objects.all()
#     return render(request,'home.html',{'m':m})

class Movielistview(ListView):
    model=Movie
    template_name="home.html"
    context_object_name="m"

# def addmovie(request):
#     form=Movieform()
#     if(request.method=="POST"):
#         form=Movieform(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return home(request)
#     return render(request,'addmovie.html',{'form':form})

class Movieaddview(CreateView):
    model=Movie
    template_name="addmovie.html"
    fields=['name','desc','year','img']
    success_url=reverse_lazy('movieapp:home')

# def moviedetail(request,p):
#     m=Movie.objects.get(id=p)
#     return render(request,'view.html',{'m':m})

class Moviedetailview(DetailView):
    model=Movie
    template_name="view.html"
    context_object_name='m'

# def updatemovie(request,p):
#     m=Movie.objects.get(id=p)
#     form=Movieform(instance=m)
#     if (request.method=="POST"):
#         form=Movieform(request.POST,request.FILES,instance=m)
#         if form.is_valid():
#             form.save()
#             return home(request)
#     return render(request,'addmovie.html',{'form':form})

class Movieupdateview(UpdateView):
    model=Movie
    template_name="addmovie.html"
    fields=['name', 'desc', 'year', 'img']
    success_url = reverse_lazy('movieapp:home')


# def deletemovie(request,p):
#     m=Movie.objects.get(id=p)
#     m.delete()
#     return home(request)

class Moviedeleteview(DeleteView):
    model=Movie
    template_name="delete.html"
    success_url = reverse_lazy('movieapp:home')