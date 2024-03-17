# projects/views.py

from django.shortcuts import render
from projects.models import Project

def home(request):
    return render(request, "projects/home.html", {})

# index view, get all rows
def project_index(request):
  projects = Project.objects.all()
  context = {
    "projects": projects
  }
  return render(request, "projects/project_index.html", context)

# detail view, get a specific row
def project_detail(request, pk):
  project = Project.objects.get(pk=pk)
  context = {
   "project": project
  }
  return render(request, "projects/project_detail.html", context)

