document.addEventListener('DOMContentLoaded', () => {
    const gameBoard = document.getElementById('game-board');
    let currentPlayer = 'X';

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



