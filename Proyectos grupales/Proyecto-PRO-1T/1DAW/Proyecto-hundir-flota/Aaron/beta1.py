import random
import string

EMPTY = ''

UNEXPLORED = '⬛'
WATER = '🟦'
TOUCHED = '🟧'
SUNKEN = '🟥'


def generate_board(
    size: int = 10,
    sheeps: tuple[tuple[int, int]] = ((5, 1), (4, 1), (3, 2), (2, 1)),
) -> list[list[str]]:
    board = [[EMPTY for _ in range(size)] for _ in range(size)]
    for sheep_size, num_sheeps in sheeps:
        placed_sheeps = 0
        while placed_sheeps < num_sheeps:
            sheep_id = f'{sheep_size}{string.ascii_uppercase[placed_sheeps]}'
            row, col = random.randint(0, size), random.randint(0, size)
            step = random.choice((-1, 1))
            row_step, col_step = (step, 0) if random.randint(0, 1) else (0, step)
            breadcrumbs = []
            for _ in range(sheep_size):
                try:
                    if not (0 <= row < size and 0 <= col < size):
                        raise IndexError()
                    if board[row][col] == EMPTY:
                        board[row][col] = sheep_id
                        breadcrumbs.append((row, col))
                    else:
                        raise IndexError()
                    row += row_step
                    col += col_step
                except IndexError:
                    # reset board
                    for bc in breadcrumbs:
                        board[bc[0]][bc[1]] = EMPTY
                    break
            else:
                placed_sheeps += 1

    return board


def show_board(board: list[list[str]]) -> None:
    for row in board:
        for item in row:
            print(f'[{item:2s}]', end='')
        print()


# TU CÓDIGO DESDE AQUÍ HACIA ABAJO
# ↓↓↓↓↓↓↓↓↓

board = generate_board()


mar = [
    ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
    ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
    ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
    ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
    ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
    ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
    ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
    ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
    ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
    ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
]

num_puntos = 0
intentos = 100
size = 10
golpes_2a = 0
golpes_3a = 0
golpes_3b = 0
golpes_4a = 0
golpes_5a = 0
barcos_hundidos = 0

# con intentos me refiero a casillas sin explorar, y como es un tablero de 10x10, son 100.

for intento in range(intentos):
    coordenadas = (input('Introduce una coordenada ')).upper()

    ld = 'ABCDEFGHIJKL'
    n = coordenadas[1:]
    l = ld.find(coordenadas[:1])

    print('la posición es fila ' f'{l}' ' y columna ' f'{n}')

    target_pos = board[int(l)][int(n)]

    if target_pos == '':
        mar[int(l)][int(n)] = '🟦'
        num_puntos -= 1
        intentos -= 1
        print('AGUA...')
        for row in range(size):
            for col in range(size):
                symbol = mar[row][col]
                print(symbol, end=' ')
            print()
        if num_puntos < 0:
            num_puntos = 0

    if target_pos != '':
        mar[int(l)][int(n)] = '🟧'
        intentos -= 1
        if target_pos == '2A':
            golpes_2a += 1
            if golpes_2a < 2:
                num_puntos += 2 * 2
                print('¡TOCADO!')
            elif golpes_2a == 2:
                barcos_hundidos += 1
                print('¡HUNDIDO!')
                num_puntos += 2 * 4
                for i in range(size):
                    for e in range(size):
                        if board[i][e] == '2A':
                            mar[i][e] = '🟥'
        if target_pos == '3A':
            golpes_3a += 1
            if golpes_3a < 3:
                num_puntos += 3 * 2
                print('¡TOCADO!')
            elif golpes_3a == 3:
                barcos_hundidos += 1
                print('¡HUNDIDO!')
                num_puntos += 3 * 4
                for i in range(size):
                    for e in range(size):
                        if board[i][e] == '3A':
                            mar[i][e] = '🟥'
        if target_pos == '3B':
            golpes_3b += 1
            if golpes_3b < 3:
                num_puntos += 3 * 2
                print('¡TOCADO!')
            elif golpes_3b == 3:
                barcos_hundidos += 1
                print('¡HUNDIDO!')
                num_puntos += 3 * 4
                for i in range(size):
                    for e in range(size):
                        if board[i][e] == '3B':
                            mar[i][e] = '🟥'
        if target_pos == '4A':
            golpes_4a += 1
            if golpes_4a < 4:
                num_puntos += 4 * 2
                print('¡TOCADO!')
            elif golpes_4a == 4:
                barcos_hundidos += 1
                print('¡HUNDIDO!')
                num_puntos += 4 * 4
                for i in range(size):
                    for e in range(size):
                        if board[i][e] == '4A':
                            mar[i][e] = '🟥'
        if target_pos == '5A':
            golpes_5a += 1
            if golpes_5a < 5:
                num_puntos += 5 * 2
                print('¡TOCADO!')
            elif golpes_5a == 5:
                barcos_hundidos += 1
                print('¡HUNDIDO!')
                num_puntos += 5 * 4
                for i in range(size):
                    for e in range(size):
                        if board[i][e] == '5A':
                            mar[i][e] = '🟥'
                num_puntos += 5 * 2
            print('¡TOCADO!')

        for row in range(size):
            for col in range(size):
                symbol = mar[row][col]
                print(symbol, end=' ')
            print()
        if num_puntos < 0:
            num_puntos = 0

    if num_puntos == 1 or num_puntos == -1:
        puntos = 'punto'
    else:
        puntos = 'puntos'
    if barcos_hundidos == 5:
        print('¡VICTORIA!')
        break

    print('puntuación =' + ' ' + f'{num_puntos}' + ' ' + f'{puntos}')
