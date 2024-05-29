from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login,logout,authenticate

# Home page
# -----------------------------------------------------------------------
def home(request):
    return render(request,"index.html")


# Register page
# -----------------------------------------------------------------------
def register(request):
    msg=None
    if request.method=='GET':
        form=CustomUserCreationForm()
    # form=UserCreationForm()
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Registeration successsfulll"
        else:
            msg="Failed"
    return render(request,'register.html',{'form':form,'msg':msg})

# user login
# =======================================
def user_login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is None:
            message = "Login Failed!!"
            return render(request,"login.html",{"message":message})
        if user is not None:
            login(request,user)
            return HttpResponseRedirect("/products/")
        
# user logout
# =======================================
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login/")


# --------------------------------------------
# Demo function
# =---------------------------------------------
def template_filter_example(request):
    data="django learning"
    return render(request,"demo.html",{"data":data})