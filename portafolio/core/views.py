from django.shortcuts import render, HttpResponse, redirect
from data import models
from presentation import forms
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'presentation/home.html')

def portafolio(request):
    projects = models.Project.objects.all()
    return render(request,'presentation/projects.html',
    {'projects': projects})

def project(request, id):
    project = models.Project.objects.get(pk=id)
    return render(request,'presentation/project_details.html',
    {'project': project})


def addproject(request):
    
    if request.method == 'POST':
        
        projectForm = forms.ProjectForm(request.POST, request.FILES)
        
        if projectForm.is_valid():
            
            projectForm.save()

            return redirect(reverse('portafolio'))
            #return redirect(reverse('addproject') + "?title=" + request.POST.get('title'))
    else:
        projectForm = forms.ProjectForm()
        return render(request,'presentation/project.html', {'form':projectForm})


def saludo(request, name='Fulanito'):
    if name == '':
        name = 'Fulanito'

    return HttpResponse('<h1>Hola ' + name + '!!!</h1>')


def browser(request):
    browser = request.META['HTTP_USER_AGENT']
    return HttpResponse('Tu navegador es ' + browser)