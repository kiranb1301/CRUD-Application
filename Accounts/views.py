from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .forms import UserModelForm
from .models import Register
from django.urls import reverse
from django.shortcuts import redirect 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def main(request): 
    #form = UserModelForm() 
    return render(request,'Base.html',{'Name':"Kiran"})  

def Add_show(request):
    if request.method=='POST':
        form1 = UserModelForm(request.POST) 
        if form1.is_valid():
                nm = form1.cleaned_data.get('name') 
                em = form1.cleaned_data.get('email')
                mm = form1.cleaned_data.get('mobile') 
                Pm = form1.cleaned_data.get('password')
                Pg = form1.cleaned_data.get('re_renter_password') 
                User1 = Register(name=nm,email=em,mobile=mm,password=Pm,re_renter_password=Pg)
                #messages.success(request,"Account Created succcessfully")
                User1.save() 
                return redirect('Add_Show') 
    else: 
        form1 = UserModelForm() 
    stud = Register.objects.all()
    return render(request,'Register1.html',{'form':form1,'Stud_data':stud})  


#This Function deletes the data permanently from Database 
def delete_data(request,id):  
    Delete1 = get_object_or_404(Register,pk=id) 
    if request.method == 'POST':
        Delete1.delete() 
        return redirect('show_students')  
    #return render(request,'AddandShow.html',{'Delete':Delete1}) 


#This function updates the student info 

def Update_data(request,id):
    #record = get_object_or_404(Register,pk=id)
    if request.method == 'POST':
        update = Register.objects.get(pk=id)
        form = UserModelForm(request.POST, instance=update)
        if form.is_valid():
            form.save() 
            return redirect('show_students')
    else:
        update = Register.objects.get(pk=id)
        form = UserModelForm(instance=update)
    return render(request, 'update.html', {'form': form, 'record': update})  

'''def user_login(request):
    if request.method == 'POST':
        form1 = AuthenticationForm(request,data=request.POST)
        if form1.is_valid():
            username = form1.cleaned_data.get('Email')
            password = form1.cleaned_data.get('Password')
            user = authenticate(request, Email=username, Password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'login.html',{'error':'Email or Password in incorrect'})
    else:
        form1 = AuthenticationForm()
    return render(request, 'login.html')'''
    # views.py

'''def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
            # Redirect to a success page
        else:
            return render(request, 'login.html',{'error':'Email or Password in incorrect'})
            # Handle invalid login
    return render(request, 'login.html')
    # Render your login template with the form'''


# Logout View
'''@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))
'''
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def show_students(request):
    stud = Register.objects.all()
    return render(request, 'User_data.html', {'Stud_data': stud}) 