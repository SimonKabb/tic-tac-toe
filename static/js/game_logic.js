document.addEventListener('DOMContentLoaded', () => {
    const gameBoard = document.getElementById('game-board');
    let currentPlayer = 'X';

    // Получаем идентификатор игры из скрытого поля
    const gameKeyElement = document.getElementById('game-key');
    const gameKey = gameKeyElement.value;

    // Функция для загрузки и отображения ходов
    function loadMoves() {
        fetch(`/get_moves/?game_key=${gameKey}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrf_token,
            },
        })
            .then(response => response.json())
            .then(data => {
                // Обработка данных о ходах и их отображение на сетке
                if (data.moves && data.moves.length > 0) {
                    data.moves.forEach(move => {
                        // Отобразить ход на сетке (например, путем изменения текста ячейки)
                        const cell = document.querySelector(`[data-row="${move.row}"][data-col="${move.col}"]`);
                        if (cell) {
                            cell.textContent = move.symbol;
                        }
                    });
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }

    // Создание игровой сетки
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            const cell = document.createElement('div');
            cell.className = 'game-cell';
            cell.dataset.row = i;
            cell.dataset.col = j;
            cell.addEventListener('click', handleClick);
            gameBoard.appendChild(cell);
        }
    }
    loadMoves();
    function handleClick(event) {
        const cell = event.target;

        if (!cell.textContent) {
            cell.textContent = currentPlayer;
            currentPlayer = (currentPlayer === 'X') ? 'O' : 'X';

            const row = cell.dataset.row;
            const col = cell.dataset.col;
            const gameKeyElement = document.getElementById('game-id');
            const gameKey = gameKeyElement.textContent;
            fetch('/make_move/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrf_token,
                },
                body: JSON.stringify({
                    row: row,
                    col: col,
                    symbol: cell.textContent,
                    game_key: gameKey,
                }),
            })
                .then(response => response.json())
                .then(data => {
                    // Обработка ответа от сервера, если необходимо
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }
    }
});



