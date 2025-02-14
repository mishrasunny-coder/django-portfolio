from django.shortcuts import render
from projects.models import Project
# from django.http import HttpResponse

# Create your views here.
# def project_list(request):
    # return HttpResponse("<h1>Hello Everyone!</h1>")
    # return render(request, 'projects/index.html')

def all_projects(request):
    # query database
    projects = Project.objects.all()
    # print(projects)
    return render(request, 'projects/all_projects.html', {'projects': projects})

def project_detail(request, pk):
    # query database
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})