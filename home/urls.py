from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.index,name="index"),
    path('index',views.index,name="index"),
    path('Register',views.profile_reg,name="Register"),
    path('registration',views.regi,name="registration"),
    path('login',views.loginuser,name="login"),
    path('logout',views.logoutuser,name="logout"),
    path('fillup',views.fillup,name="fillup")
]