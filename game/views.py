from django.shortcuts import render


def index(request):
    template = 'game/game_board.html'
    return render(request, template)
