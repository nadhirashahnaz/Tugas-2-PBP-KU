import datetime
from django.urls import reverse
from todolist.models import Task
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers

##fungsi show_todos

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    this_user = request.user
    data_todolist = Task.objects.filter(user=this_user)
    context = {
        'data_todolist': data_todolist,
        'last_login': request.COOKIES['last_login'],
        'name' : this_user
    }
    return render(request, "todolist.html", context)


@login_required(login_url='/todolist/login/')
def show_todolist_ajax(request):
    this_user = request.user
    data_todolist = Task.objects.filter(user=this_user)
    context = {
        'data_todolist': data_todolist,
        'last_login': request.COOKIES['last_login'],
        'name' : this_user
    }
    return render(request, "todolist_ajax.html", context)


def submit_ajax(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        new_data = Task(user=request.user, title=title, description=description, date=datetime.datetime.now())
        new_data.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()


@login_required(login_url='/todolist/login/')
def show_json(req):
    task_list = Task.objects.filter(user=req.user)
    return HttpResponse(serializers.serialize("json", task_list), content_type="application/json")

def get_todolist_json(request):
    tasks = Task.objects.filter(user = request.user)
    for task in tasks:
        if task.is_finished:
            task.status = 'Done'
        else:
            task.status = 'Not Yet'
    return HttpResponse(serializers.serialize('json', tasks))

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == 'POST':

        #Title dan Description
        task_title = request.POST['task_title']
        task_description = request.POST['description']

        isFill = False

        #Cek Apakah Title & Description diisi
        if(isinstance(task_title, str) and isinstance(task_description,str)):

            #Panjang 0 berarti kosong
            if (len(task_title.strip()) !=0 and len(task_description.strip()) !=0):
                isFill = True
                task = Task(title=task_title, description=task_description)
                task.user = request.user
                task.save()
                
                return redirect('todolist:show_todolist')

        #Title & Description kosong
        if(isFill == False):
            messages.info(request, 'Please fill both fields with letter(s) or number(s)')

    return render(request,'create_task.html')


# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now().strftime(("%d/%m/%Y %H:%M:%S"))))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def show_todos(request):
    data_todolist = Task.objects.filter(user = request.user)
    context = {'username': request.COOKIES['username'],
               'last_login': request.COOKIES['last_login'],
               'todos': data_todolist,
              }
    return render(request,'todolist_ajax.html', context)


@login_required(login_url='/todolist/login/')
def delete_task(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('todolist:show_todolist')


def status(request,id):
    task = Task.objects.get(id=id)
    task.is_finished= not task.is_finished
    task.save(update_fields=["is_finished"])
    return redirect('todolist:show_todolist')


@login_required(login_url='/todolist/login/')
def delete_task_ajax(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('todolist:show_todolist_ajax')


def status_ajax(request,id):
    task = Task.objects.get(id=id)
    task.is_finished= not task.is_finished
    task.save(update_fields=["is_finished"])
    return redirect('todolist:show_todolist_ajax')