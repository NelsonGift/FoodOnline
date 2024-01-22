from django.shortcuts import render,redirect
from django.http import HttpResponse

from vendor.forms import Vendorform
from .forms import Userform
from .models import User, UserProfile
from django.contrib import messages
# Create your views here.
def registerUser(request):
    if request.method == 'POST':
        # print(request.POST)
        form = Userform(request.POST)
        if form.is_valid():
            # Creating user using the form
            # password = form.cleaned_data['password']
            # user=form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()

            # Creating user using create_user method
            first_name =form.cleaned_data['first_name']
            last_name =form.cleaned_data['last_name']
            username =form.cleaned_data['username']
            email =form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.CUSTOMER
            user.save()
            print('User is created')
            messages.success(request,"Account Resgistered Successfully!")
            return redirect('registerUser')
        else:
            print("Invalid form")
            print(form.errors)
    else:
       form = Userform
    context = {
        'form': form,
    }
    return render(request, 'accounts/registerUser.html',context)


def registerVendor(request):
    if request.method=='POST':
        # store the data and create user
        form = Userform(request.POST)
        v_form= Vendorform(request.POST, request.FILES)
        if form.is_valid() and v_form.is_valid:
            first_name =form.cleaned_data['first_name']
            last_name =form.cleaned_data['last_name']
            username =form.cleaned_data['username']
            email =form.cleaned_data['email']
            password = form.cleaned_data['password']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.VENDOR
            user.save()
            vendor= v_form.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()
            messages.success(request, "Account Resgistered Successfully!Please wait for approval.")
            return redirect('registerVendor')

        else:
            print("Inavlid Form")
            print(form.errors)
    
    else:
     form = Userform()
     v_form = Vendorform()
    context={
        'form':form,
        'v_form': v_form,
    }
    return render(request,'accounts/registerVendor.html',context)