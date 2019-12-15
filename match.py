from functools import reduce

import numpy as np

STILL_LIFE = 'STILL_LIFE'
OSCILLATOR = 'OSCILLATOR'

shapes = [
    {
        'name': 'block',
        'type': STILL_LIFE,
        'pattern': np.array([
            0, 0, 0,
            0, 1, 1,
            0, 1, 1
        ], dtype=np.uint8)
    },
    {
        'name': 'blinker',
        'type': OSCILLATOR,
        'pattern': [
            np.array([
                0, 1, 0,
                0, 1, 0,
                0, 1, 0
            ], dtype=np.uint8),
            np.array([
                0, 0, 0,
                1, 1, 1,
                0, 0, 0
            ], dtype=np.uint8)
        ]
    }
]

shapes2 = [
    {
        'name': 'block',
        'type': STILL_LIFE,
        'pattern': np.array([
            [1, 1],
            [1, 1]
        ], dtype=np.uint8)
    },
    {
        'name': 'blinker',
        'type': OSCILLATOR,
        'pattern': [
            np.array([
                [1],
                [1],
                [1]
            ], dtype=np.uint8),
            np.array([
                [1, 1, 1]
            ], dtype=np.uint8)
        ]
    }
]

board = np.array([
    0, 0, 0, 0, 0, 1, 0, 0, 0,
    1, 1, 1, 0, 1, 1, 0, 0, 0,
    0, 0, 0, 0, 1, 1, 0, 1, 1,
    0, 0, 0, 0, 0, 0, 0, 1, 1
], dtype=np.uint8)

DIR_RIGHT_DIAG = 'r_diag'
DIR_LEFT_DIAG = 'l_diag'
DIR_DOWN = 'down'
DIR_RIGHT = 'right'
DIR_LEFT = 'left'
DIR_ROOT = 'root'


def explore_neighbours(board, i, j, cols, rows, ones, direction=DIR_ROOT):
    ones.append((i, j))
    if direction == DIR_RIGHT_DIAG or direction == DIR_DOWN or direction == DIR_ROOT or direction == DIR_LEFT_DIAG:
        a = board[i + 1][j] if i + 1 < rows else None
        if a == 1:
            explore_neighbours(board, i + 1, j, cols, rows, ones, direction=DIR_DOWN)

    if direction == DIR_RIGHT_DIAG or direction == DIR_ROOT:
        b = board[i + 1][j + 1] if i + 1 < rows and j + 1 < cols else None
        if b == 1:
            explore_neighbours(board, i + 1, j + 1, cols, rows, ones, direction=DIR_RIGHT_DIAG)

    if direction == DIR_RIGHT or direction == DIR_RIGHT_DIAG or direction == DIR_ROOT:
        c = board[i][j + 1] if j + 1 < cols else None
        if c == 1:
            explore_neighbours(board, i, j + 1, cols, rows, ones, direction=DIR_RIGHT)

    if direction == DIR_LEFT_DIAG or direction == DIR_LEFT:
        d = board[i][j - 1] if j - 1 >= 0 else None
        if d == 1:
            explore_neighbours(board, i, j - 1, cols, rows, ones, direction=DIR_LEFT)

    if direction == DIR_LEFT_DIAG or direction == DIR_ROOT:
        e = board[i + 1][j - 1] if i + 1 < rows and j - 1 >= 0 else None
        if e == 1:
            explore_neighbours(board, i + 1, j - 1, cols, rows, ones, direction=DIR_LEFT_DIAG)

    return ones


def clear_pattern(board, ones):
    for (i, j) in ones:
        board[i][j] = 0


def get_pattern(ones):
    min_i = reduce(lambda a, b: min(a, b[0]), np.array(ones)[1:], ones[0][0])
    max_i = reduce(lambda a, b: max(a, b[0]), np.array(ones)[1:], ones[0][0])
    min_j = reduce(lambda a, b: min(a, b[1]), np.array(ones)[1:], ones[0][1])
    max_j = reduce(lambda a, b: max(a, b[1]), np.array(ones)[1:], ones[0][1])

    si, sj = (max_i - min_i + 1, max_j - min_j + 1)
    pattern = np.zeros((si, sj), dtype=np.uint8)
    for (i, j) in ones:
        pattern[i - min_i][j - min_j] = 1

    return pattern


def match_pattern(pattern_to_check, shapes):
    for shape in shapes:
        if shape['type'] == STILL_LIFE:
            print("checking: ")
            print(shape['pattern'])
            is_same = np.array_equal(shape['pattern'], pattern_to_check)
            if is_same:
                print('Found {}'.format(shape['name']))
                break
        elif shape['type'] == OSCILLATOR:
            for pattern in shape['pattern']:
                print(pattern)
                is_same = np.array_equal(pattern, pattern_to_check)
                if is_same:
                    print('Found {}'.format(shape['name']))
                    break


def match2(board, cols, rows, shapes):
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 1:
                ones = explore_neighbours(board, i, j, cols, rows, ones=[])
                print(ones)
                # match pattern
                found_pattern = get_pattern(ones)
                print(found_pattern)
                match_pattern(found_pattern, shapes)
                # clear
                clear_pattern(board, ones)
                print("=======================")


def match():
    for i in range(2):
        for j in range(7):
            x = i * 9 + j
            y = i * 9 + 9 + j
            z = i * 9 + 18 + j

            a = np.array([
                board[x], board[x + 1], board[x + 2],
                board[y], board[y + 1], board[y + 2],
                board[z], board[z + 1], board[z + 2],
            ], dtype=np.uint8)

            print("A: ")
            print(a)
            for shape in shapes:
                if shape['type'] == STILL_LIFE:
                    print("checking: ")
                    print(shape['pattern'])
                    is_same = np.packbits(a, bitorder='little')[0] == np.packbits(shape['pattern'], bitorder='little')[
                        0]
                    if is_same:
                        print('Found {}'.format(shape['name']))
                        break
                elif shape['type'] == OSCILLATOR:
                    for pattern in shape['pattern']:
                        print(pattern)
                        is_same = np.packbits(a, bitorder='little')[0] == \
                                  np.packbits(pattern, bitorder='little')[0]
                        if is_same:
                            print('Found {}'.format(shape['name']))
                            break


if __name__ == '__main__':
    # match()
    board2 = np.array([
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1]
    ], dtype=np.uint8)
    match2(board=board2, cols=9, rows=4, shapes=shapes2)
