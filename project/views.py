from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, "project/index.html", {"projects": projects})


def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, "project/detail.html", {"project": project})

