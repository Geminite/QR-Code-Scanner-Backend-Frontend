import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import RewardPoints, Log, Allocation
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
                messages.info(request, 'Email is already used!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already used!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password is not the same!')
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
            messages.info(request, 'Credentials are invalid!')
            return redirect('login')
    
    else:
        return render(request, 'login.html')

def dashboard(request):
    callname = RewardPoints.objects.all()
    return render(request, 'dashboard.html',{'callname': callname})

def logout(request):
    auth.logout(request)
    return redirect('/')

def checking(request):
    rewards_points = RewardPoints.objects.all()

    find = 'A'
    if Allocation.objects.filter(placeholder=find).exists():
        check_allocation = '1'
        return render(request, 'checking.html',{'rewards_points': rewards_points, 'check_allocation':check_allocation})  
    
    else:
        check_allocation = '0'
        return render(request, 'checking.html',{'rewards_points': rewards_points, 'check_allocation':check_allocation})      

def backlog_list(request): 
    account_name = request.POST['account_name']
    access_log = Log.objects.filter(source=account_name).order_by('-date') #-date is used to reverse the order of the database objects
    return JsonResponse({"access_log":list(access_log.values())})

def send(request):
    receiver = request.POST['receiver']
    final_result = request.POST['final_result']

    new_message = RewardPoints.objects.filter(name=receiver).update(value=final_result)
    return HttpResponse('This has been added the account specified in the receiver.') #for some reason throws out internal error without this???

def backlog(request):
    account_name = request.POST['account_name']

    new_log = Log.objects.create(source=account_name) 
    new_log.save()

    return HttpResponse('Log is recorded')

def test_page(request):
    return render(request, 'test_page.html')

def pointsprocess(request):
    allocationobject = Allocation.objects.all()
    rewards_points = RewardPoints.objects.all()
    #initial value is zero - must change value to database(update points?) value
    return render(request, 'pointsprocess.html',{'allocationobject': allocationobject,'rewards_points': rewards_points})

def qrscript(request):
    return render(request, 'qrscript.html')

def receiver_update(request):
    account_name = request.POST['account_name']
    
    new_allocation = Allocation.objects.create(receiver=account_name)
    new_allocation.save()
    return HttpResponse('Your Reward Points are now being processed.')

def qrcode(request):
    return render(request, 'qrcode.html')

def qrlog(request):
    return render(request, 'qrlog.html')

def delete_receiver(request):
    find = 'A'
    remove_receiver = Allocation.objects.get(placeholder=find)
    remove_receiver.delete()
    return HttpResponse('Transaction has now been cleared')


