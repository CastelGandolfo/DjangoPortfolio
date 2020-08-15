from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def index(request):
    return render(request, "project/index.html")


def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, "project/detail.html", {"project": project})

