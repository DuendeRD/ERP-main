from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
    return render(request, "Dashboard.html")

def Login(request):
    return render(request, 'login.html')

def table(request):
    return render(request, 'table.html')


def dat(request):
    return render(request, 'dat.html')


def index(request):
    return render(request, 'index.html')





"""
logins = [
    {
        'username': 'admin',
        'password': 'admin'
    },
    {
        'username': 'user',
        'password': 'user'
    }
]


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        for login in logins:
            if login['username'] == username and login['password'] == password:
                return render(request, 'home.html')
        return render(request, 'login.html')
    return render(request, 'login.html')    





"""