from django.shortcuts import render,redirect
import requests
from .models import *
from django.contrib import messages


# Create your views here.

def LoginPage(request):
    return render(request,"login.html")

def LoginCheck(request):
    if request.method=="POST":

        umail = request.POST.get("email")
        upassword= request.POST.get("password")

        user=UserRegister.objects.filter(email=umail,password=upassword).first()
        user1 = UserRegister.objects.filter(username=umail,password=upassword).first()

        if user:
            # messages.success(request,"Login Successfully")
            request.session["user_name"] = user.name
            request.session["user_id"] = user.username
            request.session['user_uid'] = user.id

            return redirect('/homePage')

        elif user1:
            request.session["user_name"] = user1.name
            request.session["user_id"] = user1.username
            request.session['user_uid'] = user1.id

            return redirect('/homePage')

        else:
            messages.error(request,"Invalid Email Id Or Password")
    return render(request,"login.html")

def Logout(request):
    del request.session["user_name"]
    del request.session["user_id"]
    return redirect('/')

def RegisterPage(request):
    return render(request,"signup.html")

def RegisterDataSave(request):
    if request.method=="POST":

        uname = request.POST.get("uname")
        umail = request.POST.get("umail")
        usernameuniq = request.POST.get("username")
        upassword = request.POST.get("upassword")

        print(uname,umail,usernameuniq,upassword)

        if UserRegister.objects.filter(email=umail):
            messages.warning(request,"Email Id Already Exist")
        elif UserRegister.objects.filter(username=usernameuniq):
            messages.warning(request,"User Already Exist")
        else:
            Quairy = UserRegister(name=uname,email=umail,username=usernameuniq,password=upassword)
            Quairy.save()
            messages.success(request, "Registration SuccessFully!!!")
            return render(request,"login.html")

    return render(request,"signup.html")

def HomePage(request):

    Postdata = PosttModel.objects.all().order_by('-id')

    contex={

        "data":Postdata
    }
    return render(request,"instgram.html",contex)

def CreatePage(request):
    return render(request,"create.html")

def Post(request):
        uid = request.session['user_uid']
        image = request.FILES['images']
        Description = request.POST.get("desc")

        print(image)

        Quiry = PosttModel(nameuser=UserRegister(id=uid),photos=image,description=Description)
        Quiry.save()
        messages.success(request,"Post Upload Successfully!!")

        return redirect('/homePage')

