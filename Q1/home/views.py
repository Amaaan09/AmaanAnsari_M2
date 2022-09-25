from django.shortcuts import render, redirect
from .forms import NewProjForm
from django.contrib import messages
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate



# Create your views here.


def home(response):
    return render(response, 'index.html')

def projects(response):
    try:
        data = Task.objects.all()
        context = {
            'proj' : data
        }
    except :
        context = {
            'proj' : 'Data not Found'
        }
    return render(response, 'Task/projs.html', context)

def projectDetails(response, trial):
    # data = Task.objects.filter(name = trial)[0] # same thing as get
    data = Task.objects.get(text = trial)

    context = {'fetch' : data}
    return render(response, 'Task/projd.html', context)

def NewProject(response):
    form = NewProjForm(response.POST)

    if response.method == 'POST':
    
        if form.is_valid():
            form.save()
            messages.success(response, "Task Added Successfully")
            # yahan pe success is the message.info

            return redirect('proj')

    context = {"form" : form}
    return render(response, 'Task/newproj.html', context)

def DelProject(response, id):
    data = Task.objects.get(id=id)
    data.delete()

    messages.warning(response, "Task Deleted Successfully")

    return redirect('proj')

def UpProject(response, id):
    data = Task.objects.get(id=id)
    Upform = NewProjForm(response.POST or None, instance=data)
    
    if Upform.is_valid():
        Upform.save()
        messages.success(response, "Task Updated Successfully")

        return redirect('proj')

    context = {"form" : Upform}
    return render(response, 'Task/ProjectUpdate.html', context)



def login_page(response):
    if response.method == 'POST':
        name = response.POST['user_name']
        passu = response.POST['user_pass']

        user = authenticate(response, username= name, password = passu)
        if user is not None:
            login(response, user)
            messages.success(response, "Logged In Successfully")
            return redirect('home')
        
        else:
            print('error credentials not found')
        
            # message pass karwa do 
            return redirect('home')
        
    return render(response, 'login.html')


def logout_page(response):
    logout(response)
    return redirect('home')



def signup_auth(request):
    if request.method == 'POST':
        user = request.POST['Name']
        email = request.POST['email']
        password1 = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password1 == confirmpassword:
            if not User.objects.filter(username=user).exists():
                if not User.objects.filter(email=email).exists():
                    user=User.objects.create_user(username = user, email = email, password=password1)
                    user.save()
                    print("New User Created")
                    login(request, user)
        return redirect('home')
    return render(request,'signup.html')




