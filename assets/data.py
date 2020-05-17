from enum import Enum
import colorama


class Direction(Enum):
    LEFT = -1
    RIGHT = 1
    UP = -1
    DOWN = 1
    SAME = 0


keyboard_to_direction = {
    'w': [Direction.UP, Direction.SAME],
    's': [Direction.DOWN, Direction.SAME],
    'd': [Direction.SAME, Direction.RIGHT],
    'a': [Direction.SAME, Direction.LEFT],
    'd+w': [Direction.UP, Direction.RIGHT],
    'a+w': [Direction.UP, Direction.LEFT],
    'd+s': [Direction.DOWN, Direction.RIGHT],
    'a+s': [Direction.DOWN, Direction.LEFT]
}


city_elements = ['░', '░', '░', '≡', '≡',  '░', '░', '≡', '▀', '▲', '∩',
                 colorama.Fore.LIGHTYELLOW_EX + '¥' + colorama.Fore.LIGHTBLACK_EX]


text = {
    'instructions': colorama.Fore.LIGHTCYAN_EX + colorama.Style.BRIGHT \
                   + '\n\nSolve the maze of the gray and industrial city.\n' \
                     'Move around buildings, towers and parking spots and bring the music home.' \
                   + colorama.Fore.LIGHTYELLOW_EX + colorama.Style.NORMAL \
                   + '\n\n\nINSTRUCTIONS \n============\n' \
                   + colorama.Style.RESET_ALL \
                   + 'Movement:  w/a/s/d (combine w+d for example for diagonal movement)\n' \
                     '    Goal:  Reach the ⌂\n' \
                     '   Start:  press \'s\'\n' \
                     '    Quit:  press \'esc\'\n',
    'game_beat': 'You beat the game :)...so far! TA DA DAAAAAAAA',
    'exit_screen': 'Game quit'
}

