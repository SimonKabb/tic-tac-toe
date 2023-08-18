document.addEventListener('DOMContentLoaded', () => {
    const gameBoard = document.getElementById('game-board');

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
        const row = cell.dataset.row;
        const col = cell.dataset.col;

        // Отправка данных на сервер (используйте AJAX или Fetch)
        // Пример:
        fetch(`/make_move/?row=${row}&col=${col}`)
            .then(response => response.json())
            .then(data => {
                // Обновление игрового поля с учетом ответа от сервера
                // Например, обновление содержимого ячейки на "X" или "O"
            })
            .catch(error => console.error('Error:', error));
    }
});
