from django.shortcuts import render,redirect
from django.views.generic import FormView,CreateView,TemplateView,View
from django.contrib.auth import authenticate,login,logout
from socialapp.forms import RegirstrationForms,LoginForm
from django.urls import reverse

class SignUpView(CreateView):
    template_name="register.html"
    form_class=RegirstrationForms

    def get_success_url(self) :
        return reverse("signin")
class SignInView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            userobject=authenticate(request,username=uname,password=pwd)
            if userobject:
                login(request,userobject)
                print("login succesfuly")
            return redirect("index")
        print("error in login")
        return render(request,"login.html",{"form":form})
    
class IndexView(TemplateView):
    template_name="index.html"

class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")







