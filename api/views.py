import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import RewardPoints, Log
from django.http import HttpResponse, JsonResponse
# Create your views here.
def root(request):
    return render(request, 'root.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Passwod is not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None: 
            auth.login(request, user)
            if RewardPoints.objects.filter(name=username).exists():
                return redirect('dashboard')
            else:
                id = RewardPoints.objects.create(name=username)
                return redirect('dashboard')

        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    
    else:
        return render(request, 'login.html')

def dashboard(request):
    callname = RewardPoints.objects.all()
    return render(request, 'dashboard.html',{'callname': callname})

def logout(request):
    auth.logout(request)
    return redirect('/')

def qrscanner(request):
    return render(request, 'qrscanner.html')

def checking(request):
    rewards_points = RewardPoints.objects.all()
    return render(request, 'checking.html',{'rewards_points': rewards_points})  #initial value is zero - must change value to database value

def backlog_list(request): 
    account_name = request.POST['account_name']
    access_log = Log.objects.filter(source=account_name)
    return JsonResponse({"access_log":list(access_log.values())})

def send(request):
    account_name = request.POST['account_name']
    final_result = request.POST['final_result']

    new_message = RewardPoints.objects.filter(name=account_name).update(value=final_result)
    return HttpResponse('Message sent successfully') #for some reason throws out internal error without this???

def backlog(request):
    account_name = request.POST['account_name']

    new_log = Log.objects.create(source=account_name) 
    new_log.save()
    return HttpResponse('Log is recorded')

def result(request):
    return render(request, 'result.html')

def test_page(request):
    return render(request, 'pages-register.html')

def test_try(request):

    room = request.POST['room_id']


    new_message = RewardPoints.objects.create(name=room)
    new_message.save()
    return HttpResponse('Message sent successfully')