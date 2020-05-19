# coding: utf-8
from enum import Enum
import colorama
import itertools


class Instructions(Enum):
    LEFT = -1
    RIGHT = 1
    UP = -1
    DOWN = 1
    SAME = 0
    BOMB = 2
    TEST = 3


keyboard_to_direction = {
    'w': [Instructions.UP, Instructions.SAME],
    's': [Instructions.DOWN, Instructions.SAME],
    'd': [Instructions.SAME, Instructions.RIGHT],
    'a': [Instructions.SAME, Instructions.LEFT],
    'd+w': [Instructions.UP, Instructions.RIGHT],
    'a+w': [Instructions.UP, Instructions.LEFT],
    'd+s': [Instructions.DOWN, Instructions.RIGHT],
    'a+s': [Instructions.DOWN, Instructions.LEFT],
    'e+q': [Instructions.BOMB, Instructions.BOMB],
    'z': [Instructions.TEST, Instructions.TEST]
}


data = {
    'city_elements': ['░', '░', '░', '≡', '≡',  '░', '░', '≡', '▀', '▲', '∩',
                      colorama.Fore.LIGHTYELLOW_EX + '¥' + colorama.Fore.LIGHTBLACK_EX],
    'radius_three_blocks': [offset for offset in itertools.product(range(-4, 5, 1), repeat=2) if offset != (0,0)],
    'explosion_steps': {
        'one': {
            'radius_offsets': [range(-4, 5, 1), range(-3, 4, 1), range(-2, 3, 1), range(-1, 2, 1)],
            'colors': [' ',
                       colorama.Back.RED + ' ' + colorama.Back.BLACK,
                       colorama.Back.WHITE + ' ' + colorama.Back.BLACK,
                       colorama.Back.LIGHTWHITE_EX + ' ' + colorama.Back.BLACK]
        },
        'two': {
            'radius_offsets': [range(-4, 5, 1), range(-3, 4, 1), range(-2, 3, 1), range(-1, 2, 1)],
            'colors': [colorama.Back.YELLOW + ' ' + colorama.Back.BLACK,
                       colorama.Back.WHITE + ' ' + colorama.Back.BLACK,
                       colorama.Back.LIGHTWHITE_EX + ' ' + colorama.Back.BLACK,
                       colorama.Back.LIGHTWHITE_EX + ' ' + colorama.Back.BLACK]
        },
        'three': {
            'radius_offsets': [range(-4, 5, 1), range(-3, 4, 1), range(-2, 3, 1), range(-1, 2, 1)],
            'colors': [colorama.Back.WHITE + ' ' + colorama.Back.BLACK,
                       colorama.Back.LIGHTYELLOW_EX + ' ' + colorama.Back.BLACK,
                       colorama.Back.LIGHTYELLOW_EX + ' ' + colorama.Back.BLACK,
                       colorama.Back.LIGHTRED_EX + ' ' + colorama.Back.BLACK]
        },
        'four': {
            'radius_offsets': [range(-4, 5, 1), range(-3, 4, 1), range(-2, 3, 1), range(-1, 2, 1)],
            'colors': [colorama.Back.RED + ' ' + colorama.Back.BLACK,
                       colorama.Back.LIGHTRED_EX + ' ' + colorama.Back.BLACK,
                       colorama.Back.RED + ' ' + colorama.Back.BLACK,
                       ' ']
        },
        'five': {
            'radius_offsets': [range(-4, 5, 1), range(-3, 4, 1), range(-2, 3, 1), range(-1, 2, 1)],
            'colors': [' ',
                       colorama.Back.RED + ' ' + colorama.Style.DIM + colorama.Back.BLACK,
                       colorama.Back.RED + ' ' + colorama.Back.BLACK,
                       ' ']
        },
        'six': {
            'radius_offsets': [range(-4, 5, 1), range(-3, 4, 1), range(-2, 3, 1), range(-1, 2, 1)],
            'colors': [' ',
                       colorama.Back.RED + ' ' + colorama.Back.BLACK,
                       ' ',
                       ' ']
        },
        'seven': {
            'radius_offsets': [range(-4, 5, 1), range(-3, 4, 1), range(-2, 3, 1), range(-1, 2, 1)],
            'colors': [' ',
                       ' ',
                       ' ',
                       ' ']
        }

    }

}


text = {
    'instructions': [colorama.Fore.LIGHTCYAN_EX + colorama.Style.BRIGHT
                     + 'Solve the maze of the gray blade-runner-esque landscape.',
                     'Run around abandoned buildings, towers and tunnels and bring the music home.',
                     colorama.Fore.LIGHTYELLOW_EX + colorama.Style.NORMAL +
                     'INSTRUCTIONS',
                     '============' + colorama.Style.RESET_ALL,
                     'Movement:  press \'w/a/s/d\' (combine \'w+d\' for example for diagonal movement)',
                     '    Goal:  Reach the ⌂',
                     'Use bomb:  press \'q+e\' YOU ONLY HAVE 3',
                     '   Start:  press \'s\'',
                     '    Quit:  press \'esc\''],
    'game_begin': 'You have 1 minute. GO',
    'game_beat': 'You beat the game :)...for now!! TA DA DAAAAAAAA',
    'exit_screen': 'Game quit'
}

