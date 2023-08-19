from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Game, Move


def index(request):
    template = 'game/game_board.html'
    return render(request, template)


def get_data(request):
    data = {
        'key1': 'value1',
        'key2': 'value2'
    }
    return JsonResponse(data)


@csrf_exempt
def make_move(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        row = data['row']
        col = data['col']
        symbol = data['symbol']
        # Предположим, что вы передаете идентификатор игры
        game_id = data['game_id']
        player = request.user

        try:
            # Предположим, что у вас есть модель Game
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            response_data = {'message': 'Игра не найдена'}
            return JsonResponse(response_data, status=400)

        move = Move(game=game, row=row, col=col, symbol=symbol, player=player)
        move.save()

        response_data = {'message': 'Ход успешно записан'}
        return JsonResponse(response_data)
    else:
        response_data = {'message': 'Недопустимый метод запроса'}
        return JsonResponse(response_data)
