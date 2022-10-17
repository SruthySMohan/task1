from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('reg_form/', views.reg_form, name='reg_form'),
    path('reg1/', views.reg1, name='reg1'),
    path('form/', views.form, name='form'),
    path('logout/', views.logout, name='logout'),
    path('form/form/submit/',views.submit,name='submit'),


]