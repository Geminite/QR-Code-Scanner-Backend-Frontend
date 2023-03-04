from django.urls import path
from . import views

urlpatterns = [
    path('',views.root, name='root'),   #root directory
    path('register', views.register, name='register'),  #register page
    path('login', views.login, name='login'),    #login page 
    path('dashboard', views.dashboard, name='dashboard'),    #dashboard page
    path('logout', views.logout, name="logout"), #logout page
    path('qrscanner', views.qrscanner, name="qrscanner"), #QR Code Scanner
    path('checking', views.checking, name="checking"), #QR Code Scanner2
    path('result', views.result, name="result"), 
    path('send', views.send, name="send"),
    path('test_page', views.test_page, name="test_page"),
    path('test_try', views.test_try, name="test_try"),
    path('backlog', views.backlog, name="backlog"),
    path('backlog_list', views.backlog_list, name="backlog_list"),
    path('qrgenerator', views.qrgenerator, name="qrgenerator"), #QR Code Generator
    path('pointsprocess', views.pointsprocess, name="pointsprocess"), #Points Processing Page
    path('qrscript', views.qrscript, name="qrscript"), #Page containing the script that will be executed after scaning the QR Code
    path('receiver_update', views.receiver_update, name="receiver_update"), #Allows redirection to the receiver_update function
    path('qrcode', views.qrcode, name="qrcode"),
    path('delete_receiver', views.delete_receiver, name="delete_receiver")
]