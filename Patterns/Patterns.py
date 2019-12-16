import numpy as np

STILL_LIFE = 'STILL_LIFE'
OSCILLATOR = 'OSCILLATOR'
SPACESHIP = 'SPACESHIP'


patterns = [
    {
        'name': 'Block',
        'type': STILL_LIFE,
        'pattern': np.array([
            [1, 1],
            [1, 1]
        ], dtype=np.uint8)
    },
    {
        'name': 'Bee-hive',
        'type': STILL_LIFE,
        'pattern': np.array([
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [0, 1, 1, 0]
        ], dtype=np.uint8)
    },
    {
        'name': 'Loaf',
        'type': STILL_LIFE,
        'pattern': np.array([
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [0, 1, 0, 1],
            [0, 0, 1, 0]
        ], dtype=np.uint8)
    },
    {
        'name': 'Boat',
        'type': STILL_LIFE,
        'pattern': np.array([
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 0]
        ], dtype=np.uint8)
    },
    {
        'name': 'Ship',
        'type': STILL_LIFE,
        'pattern': np.array([
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 1]
        ], dtype=np.uint8)
    },
    {
        'name': 'Tub',
        'type': STILL_LIFE,
        'pattern': np.array([
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]
        ], dtype=np.uint8)
    },
    {
        'name': 'Pond',
        'type': STILL_LIFE,
        'pattern': np.array([
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 0]
        ], dtype=np.uint8)
    },
    {
        'name': 'Blinker',
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
    },
    {
        'name': 'Toad',
        'type': OSCILLATOR,
        'pattern': [
            np.array([
                [0, 0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0, 0]
            ], dtype=np.uint8),
            np.array([
                [0, 0, 1, 0],
                [1, 0, 0, 1],
                [1, 0, 0, 1],
                [0, 1, 0, 0]
            ], dtype=np.uint8)
        ]
    },
    {
        'name': 'Beacon',
        'type': OSCILLATOR,
        'pattern': [
            np.array([
                [1, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 0, 1, 1],
                [0, 0, 1, 1]
            ], dtype=np.uint8),
            np.array([
                [1, 1, 0, 0],
                [1, 0, 0, 0],
                [0, 0, 0, 1],
                [0, 0, 1, 1]
            ], dtype=np.uint8)
        ]
    },
    {
        'name': 'Pulsar',
        'type': OSCILLATOR,
        'pattern': [
            np.array([
                [0,0,1,1,1,0,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,1,0,1,0,0,0,0,1],
                [1,0,0,0,0,1,0,1,0,0,0,0,1],
                [1,0,0,0,0,1,0,1,0,0,0,0,1],
                [0,0,1,1,1,0,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,1,1,1,0,0,0,1,1,1,0,0],
                [1,0,0,0,0,1,0,1,0,0,0,0,1],
                [1,0,0,0,0,1,0,1,0,0,0,0,1],
                [1,0,0,0,0,1,0,1,0,0,0,0,1],
                [0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,1,1,1,0,0,0,1,1,1,0,0]], dtype=np.uint8),
            np.array([
                 [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0],
                 [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0],
                 [0,0,0,0,1,1,0,0,0,1,1,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [1,1,1,0,0,1,1,0,1,1,0,0,1,1,1],
                 [0,0,1,0,1,0,1,0,1,0,1,0,1,0,0],
                 [0,0,0,0,1,1,0,0,0,1,1,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,1,1,0,0,0,1,1,0,0,0,0],
                 [0,0,1,0,1,0,1,0,1,0,1,0,1,0,0],
                 [1,1,1,0,0,1,1,0,1,1,0,0,1,1,1],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,1,1,0,0,0,1,1,0,0,0,0],
                 [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0],
                 [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0]], dtype=np.uint8),
            np.array([
                 [0,0,1,1,0,0,0,0,0,1,1,0,0],
                 [0,0,0,1,1,0,0,0,1,1,0,0,0],
                 [1,0,0,1,0,1,0,1,0,1,0,0,1],
                 [1,1,1,0,1,1,0,1,1,0,1,1,1],
                 [0,1,0,1,0,1,0,1,0,1,0,1,0],
                 [0,0,1,1,1,0,0,0,1,1,1,0,0],
                 [0,0,0,0,0,0,0,0,0,0,0,0,0],
                 [0,0,1,1,1,0,0,0,1,1,1,0,0],
                 [0,1,0,1,0,1,0,1,0,1,0,1,0],
                 [1,1,1,0,1,1,0,1,1,0,1,1,1],
                 [1,0,0,1,0,1,0,1,0,1,0,0,1],
                 [0,0,0,1,1,0,0,0,1,1,0,0,0],
                 [0,0,1,1,0,0,0,0,0,1,1,0,0]], dtype=np.uint8)
        ]
    },
    {
        'name': 'Glider',
        'type': SPACESHIP,
        'pattern': [
            np.array([
                [0,1,0],
                [0,0,1],
                [1,1,1]
            ], dtype=np.uint8),
            np.array([
                [1,0,0],
                [0,1,1],
                [1,1,0]
            ], dtype=np.uint8)
        ]
    },
    {
        'name': 'Lightweight',
        'type': SPACESHIP,
        'pattern': [
            np.array([
                 [0,1,0,0,1],
                 [1,0,0,0,0],
                 [1,0,0,0,1],
                 [1,1,1,1,0]], dtype=np.uint8),
            np.array([
                 [1,1,0,0,],
                 [1,0,1,1,],
                 [1,1,1,1,],
                 [0,1,1,0,]], dtype=np.uint8)
        ]
    }
]
