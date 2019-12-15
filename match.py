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

board = np.array([
    0, 0, 0, 0, 0, 1, 0, 0, 0,
    1, 1, 1, 0, 1, 1, 0, 0, 0,
    0, 0, 0, 0, 1, 1, 0, 1, 1,
    0, 0, 0, 0, 0, 0, 0, 1, 1
], dtype=np.uint8)


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
                elif shape['type'] == OSCILLATOR:
                    for pattern in shape['pattern']:
                        print(pattern)
                        is_same = np.packbits(a, bitorder='little')[0] == \
                                  np.packbits(pattern, bitorder='little')[0]
                        if is_same:
                            print('Found {}'.format(shape['name']))
                            break


if __name__ == '__main__':
    match()