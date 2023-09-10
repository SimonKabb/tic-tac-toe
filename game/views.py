from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Game, Move
import random
import string


def generate_unique_key():
    while True:
        game_key = ''.join(random.choices(string.digits, k=8))
        if not Game.objects.filter(game_key=game_key).exists():
            return game_key


def index(request):
    template = 'game/new_game.html'
    return render(request, template)


def get_moves(request):
    if request.method == 'GET':
        game_key = request.GET.get('game_key')
        if game_key is not None:
            game = get_object_or_404(Game, game_key=game_key)
            moves = Move.objects.filter(
                game=game).values('row', 'col', 'symbol')
            print(moves, game_key)
            return JsonResponse({'moves': list(moves)})
        else:
            return JsonResponse({'error': 'Invalid game_id'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


def new_game(request):
    game_key = generate_unique_key()
    new_game = Game.objects.create(game_key=game_key)
    new_game.save()
    return redirect('game_board', game_key=game_key)


def game_board(request, game_key):
    template = 'game/game_board.html'
    context = {'game_key': game_key}
    return render(request, template, context)


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
        game_key = data['game_key']
        player = request.user
        try:
            game = Game.objects.get(game_key=game_key)
            print('Игра найдена')
        except Game.DoesNotExist:
            response_data = {'message': 'Игра не найдена'}
            return JsonResponse(response_data, status=400)
        existing_move = Move.objects.filter(
            game=game, row=row, col=col).first()
        if existing_move:
            response_data = {'message': 'Такой ход уже был'}
            print('Такой ход уже был')
            return JsonResponse(response_data, status=400)
        move = Move(game=game, row=row, col=col, symbol=symbol, player=player)
        move.save()

        response_data = {'message': 'Ход успешно записан'}
        return JsonResponse(response_data)
    else:
        response_data = {'message': 'Недопустимый метод запроса'}
        return JsonResponse(response_data)
