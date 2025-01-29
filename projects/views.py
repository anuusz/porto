from django.shortcuts import render
from .models import Project

def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'projects/projects_list.html', {'projects': all_projects})
