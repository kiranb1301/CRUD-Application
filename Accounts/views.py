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
from .forms import LoginForm 
from django.contrib.auth.models import User
# Create your views here.
def main(request): 
    
    #form = UserModelForm() 
    return render(request,'Base.html',{'Name':"Kiran"})  

'''def Add_show(request):
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

'''
def Add_show(request):
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            Register.objects.create(
                user=user,
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                mobile=form.cleaned_data['mobile'],
                password=form.cleaned_data['password'],
                re_renter_password=form.cleaned_data['re_renter_password']
            )
            return redirect('login')
    else:
        form = UserModelForm()
    return render(request, 'Register1.html', {'form': form})
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

def user_login(request):
    if request.method == 'POST':
        form1 = LoginForm(request.POST)
        if form1.is_valid():
            email = form1.cleaned_data['email']
            password = form1.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Replace 'home' with your desired redirect URL
            else:
                return render(request, 'login.html',{'error':'Email or Password in incorrect','form':form1})
    else:
        form1 = LoginForm()
    return render(request, 'login.html',{'form':form1})
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