from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html',context={'req':dir(request),'rquest':request})

from .models import  User
def reqform(request):
    if request.method == 'GET' and request.GET:
        try:
            username = request.GET['username']
            username = request.GET.get('username')
            password = request.GET.get('password')
            email = request.GET.get('email')
            phone = request.GET.get('phone')
        except:
            pass
        print(username,password,email,phone)
    if request.method == 'POST' and request.POST:
        try:
            username = request.POST['username']
            password = request.POST.get('password')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            if username != None:
                user = User.objects.create(
                    username = username,
                    password = password,
                    email = email,
                    phone = phone
                )

                user.save()
                return JsonResponse({'status':'success'})
            else:
                return JsonResponse({'status':'success'})
        except:
            pass
    return render(request,'reqform.html')
from .forms import UserForm
def formTest(request):
    obj = UserForm()
    return  render(request,'formtest.html',{'obj':obj})