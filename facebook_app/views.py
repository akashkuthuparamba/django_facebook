from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . forms import Loginform,Createform ,Profileform
from . models import Log_in

# Create your views here.
def home(request):
    context={
        object:None
    }
    return render(request,'templates/home.html',context)


def login(request):
    form=Loginform(request.POST)
    context={}
    context["form"]=form
    
    if request.method=='POST':
        context={}
        
        
        username=request.POST['username']
        password=request.POST['password']
        context["username"]=username
        
        


        if Log_in.objects.filter(username=username).exists():
            if Log_in.objects.filter(password=password).exists():
        
                return render(request,'templates/home.html',context)
            else:
                return HttpResponse("password is wrong try again")   
        else:
            return HttpResponse("username is wrong try again")  
    return render(request,'templates/login.html',context)


def create(request):
    
    context={}
    form=Createform(request.POST or None)
    context["form"]=form
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/login/')


    return render(request,'templates/create.html',context)



def profile(request,username):
    context={}
    obj=Log_in.objects.get(username=username)
    print(obj)
    context['object']=obj
    return render(request,'profile.html',context)


def create_profile(request,id):
    context={}
    form=Profileform(request.POST or None)
    context["form"]=form
    det=request.POST
    obj=Log_in.objects.get(id=id)
    username=obj.username
    print(username)
    if form.is_valid():
        obj.first_name=request.POST['first_name']
        obj.last_name=request.POST['last_name']
        obj.email=request.POST['email']
        obj.phone_no=request.POST['phone_no']
        obj.education=request.POST['education']
        obj.place=request.POST['place']
        obj.save()

        return HttpResponse("your bio will changed")



    return render(request,'templates/profile_create.html',context)