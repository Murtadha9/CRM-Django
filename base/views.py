from django.shortcuts import render , redirect

from .forms import LoginForm , CreateUserForm, AddClient , UpdateClient
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from . models import Client
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request , 'base/index.html')




def register(request):

    form=CreateUserForm()

    if request.method =='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , 'account created successfully')
            return redirect('dashBoard')
        
    context={'form':form} 
    return render(request , 'base/register.html' , context)




def loginPage(request):
    form=LoginForm()

    if request.method =='POST':
        form=LoginForm(request , data=request.POST)

        if form.is_valid():

            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request , username=username , password=password)

            if user is not None:
                auth.login(request ,user)
                messages.success(request , 'you have logged in')
                return redirect('dashBoard')
            
    context={'form':form}    
    return render(request , 'base/login.html' , context)    

def LogOUTuser(request):
    auth.logout(request)
    messages.success(request , 'Log Out success!')
    return redirect ('loginPage')


@login_required(login_url='loginPage')
def dashBoard(request):

    clients=Client.objects.all()
    context={'clients':clients}

    return render(request , 'base/dashboard.html' , context)


@login_required(login_url='loginPage')
def create(request):
    form=AddClient()

    if request.method =='POST':
        form=AddClient(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , 'your client has add')
            return redirect('dashBoard')
        
    context={'form':form}
    return render(request , 'base/create.html', context)



@login_required(login_url='loginPage')
def updateClient(request ,pk):

    client=Client.objects.get(id=pk)
    form=UpdateClient(instance=client)

    if request.method == 'POST':
        form=UpdateClient(request.POST ,instance=client)
        if form.is_valid():
            form.save()
            messages.success(request , 'update done')
            return redirect('dashBoard')
        

    context={'form':form}
    return render(request , 'base/update.html', context)



@login_required(login_url='loginPage')
def viewClient(request ,pk):
    clientInfo=Client.objects.get(id=pk)
    context={'clientInfo':clientInfo}
    return render(request , 'base/view.html' , context)



@login_required(login_url='loginPage')
def delete(request,pk):
    client=Client.objects.get(id=pk)
    client.delete()
    messages.success(request , 'the client deleted')
    return redirect ('dashBoard')