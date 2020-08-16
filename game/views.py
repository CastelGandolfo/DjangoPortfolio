from django.shortcuts import render

def game_start(request):
    return render(request, "game/start.html")
