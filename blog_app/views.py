from django.shortcuts import render,redirect
from django.views.generic import ListView

from .forms import blog_form
from .models import blog_model



# Create your views here.
class homepage(ListView):
    model = blog_model
    template_name = 'homepage.html'

class blog_create(ListView):
    model = blog_model
    template_name = 'create.html'

def displayform(request):
    form_obj = blog_form()
    return render(request,'create.html',{'form':form_obj})


def blog_add(request):
    if request.method == "POST":
        data = blog_form(request.POST)
        if data.is_valid():

            data.save()
            return redirect('/')
        else:
            form_obj = blog_form()
            return render(request, 'create.html', {'form': form_obj})

def display_blog(request):
    record = blog_model.objects.all()
    return render(request,'read.html',{'rec':record})

def search_blog(request):


    if request.method == "GET":
        searched = request.GET.get('searched')
        # data = (blog_model.objects.all().values())
        data=blog_model.objects.all().filter(title=searched)

        return render(request, 'search.html', {'searched': searched, 'data': data})
    else:
        return render(request, 'search.html', {})
    # query = request.Get['query']
    # filter_data = blog_model.objects.filter(title__icontains=query)
    # data = {'filter_data': filter_data}
    # return render(request, 'search.html', {'searched': searched, 'data': data})

















def edit_blog(request,id):
    records = blog_model.objects.get(id=id)
    return render(request,'edit.html',{'record':records})

def update_blog(request,id):
    task = blog_model.objects.get(id=id)
    if request.method=="POST":
        data = blog_form(request.POST,instance=task)
        if data.is_valid():
            data.save()
            return redirect('/display')
    else:
        form_obj = blog_form()
        return render(request,'homepage.html', {'form': form_obj})

def delete_blog(request,id):
    task = blog_model.objects.get(id=id)
    task.delete()
    return redirect('/display')

