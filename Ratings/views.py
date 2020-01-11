from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile,Projects

# Create your views here.
# @login_required(login_url = '/accounts/login/')
def home(request):
    '''
    View function to render thr home page
    '''
    all_projects = Projects.all_projects()
    return render(request,'home.html',{'all_projets':all_projects})


