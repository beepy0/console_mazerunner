# coding: utf-8
from enum import Enum
import colorama


class Instructions(Enum):
    LEFT = -1
    RIGHT = 1
    UP = -1
    DOWN = 1
    SAME = 0
    BOMB = 2


keyboard_to_direction = {
    'w': [Instructions.UP, Instructions.SAME],
    's': [Instructions.DOWN, Instructions.SAME],
    'd': [Instructions.SAME, Instructions.RIGHT],
    'a': [Instructions.SAME, Instructions.LEFT],
    'd+w': [Instructions.UP, Instructions.RIGHT],
    'a+w': [Instructions.UP, Instructions.LEFT],
    'd+s': [Instructions.DOWN, Instructions.RIGHT],
    'a+s': [Instructions.DOWN, Instructions.LEFT],
    'e+q': [Instructions.BOMB, Instructions.BOMB]
}


city_elements = ['░', '░', '░', '≡', '≡',  '░', '░', '≡', '▀', '▲', '∩',
                 colorama.Fore.LIGHTYELLOW_EX + '¥' + colorama.Fore.LIGHTBLACK_EX]


text = {
    'instructions': [colorama.Fore.LIGHTCYAN_EX + colorama.Style.BRIGHT
                     + 'Solve the maze of the gray and industrial city.',
                     'Move around buildings, towers and parking spots and bring the music home.',
                     colorama.Fore.LIGHTYELLOW_EX + colorama.Style.NORMAL +
                     'INSTRUCTIONS',
                     '============' + colorama.Style.RESET_ALL,
                     'Movement:  w/a/s/d (combine w+d for example for diagonal movement)',
                     '    Goal:  Reach the ⌂',
                     '   Start:  press \'s\'',
                     '    Quit:  press \'esc\''],
    'game_begin': 'You have 1 minute. GO',
    'game_beat': 'You beat the game :)...so far! TA DA DAAAAAAAA',
    'exit_screen': 'Game quit'
}

