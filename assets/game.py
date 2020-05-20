# coding: utf-8
import keyboard
import shutil
import random
import threading
import time
import colorama
import itertools
from assets.data import Instructions, data, text
from datetime import datetime, timedelta


class Game:
    # TODO add some of the functions as static methods
    def __init__(self):
        self.start_time = None
        self.player_map = []
        self.map_coords = {}
        self.player_prev_pos = {'x': 1, 'y': 1}
        self.player_pos = {'x': 1, 'y': 1}
        self.player_bombs = 3
        self.bomb_timeout = datetime.now() + timedelta(seconds=0.7)
        self.lock = threading.Event()
        self.instructions = text.get('instructions', 'missing instructions')
        self.begin_screen_text = text.get('game_begin', 'missing game begin text')
        self.beat_screen_text = text.get('game_beat', 'missing game beat text')
        self.exit_screen_text = text.get('exit_screen', 'missing exit screen text')

    def init_level(self):
        for line in range(shutil.get_terminal_size()[1] - 2):
            self.player_map.append([])
            for cell in range(shutil.get_terminal_size()[0] - 1):
                if line > shutil.get_terminal_size()[1] - 12 and cell > shutil.get_terminal_size()[0] - 25:
                    self.player_map[line].append(' ')
                    continue
                self.player_map[line].append(' ' if random.randint(0, 10) < 8 else random.choice(data['city_elements']))
        self.player_map[-5][-12] = '⌂'

        self.player_map[self.player_pos['y']][self.player_pos['x']] = '♫'
        for row_ind, line in enumerate(self.player_map):
            for col_ind, cell in enumerate(line):
                self.map_coords[(row_ind, col_ind)] = cell

    def wait_quit(self, hotkey=None, suppress=False, trigger_on_release=False):
        """
        Blocks the program execution until the given hotkey is pressed. The wait lock can be released via lock.set().
        Warning: lock.set() is an end-condition operation currently, as it will free the global lock variable for all
        cases in code.
        """
        if hotkey:
            remove = keyboard.add_hotkey(hotkey, lambda: self.lock.set(),
                                         suppress=suppress, trigger_on_release=trigger_on_release)
            self.lock.wait()
            keyboard.remove_hotkey(remove)
        else:
            raise ValueError('please supply a hotkey to wait for')

    def process_keypress(self, directions):
        if directions[0] == Instructions.BOMB and directions[1] == Instructions.BOMB:
            if self.player_bombs > 0:
                detonate_bomb(self)
            return

        if self.start_time + timedelta(seconds=60) < datetime.now():
            self.exit_screen_text = 'Time ran out'
            self.lock.set()
            return

        if directions == [Instructions.SAME, Instructions.SAME]:
            return

        next_step = self.map_coords.get(
            (self.player_pos['y'] + directions[0].value, self.player_pos['x'] + directions[1].value), 'out of bounds'
        )
        if next_step == ' ':
            # reset current map board and its coordinates
            self.map_coords[(self.player_pos['y'], self.player_pos['x'])], \
                self.player_map[self.player_pos['y']][self.player_pos['x']] = ' ', ' '
            # get player's new position
            self.player_prev_pos['y'], self.player_prev_pos['x'] = self.player_pos['y'], self.player_pos['x']
            self.player_pos['y'], self.player_pos['x'] = \
                self.player_pos['y'] + directions[0].value, self.player_pos['x'] + directions[1].value
            # update current map board and its coordinates with new player position
            self.map_coords[(self.player_pos['y'], self.player_pos['x'])], \
                self.player_map[self.player_pos['y']][self.player_pos['x']] = '♫', '♫'

            update_screen(self, [self.player_prev_pos['y']])
            update_screen(self, [self.player_pos['y']])
        elif next_step == '⌂':
            self.exit_screen_text = text.get('game_beat', 'game beat text is not supplied')
            self.lock.set()
            return


def detonate_bomb(game):
    if datetime.now() <= game.bomb_timeout:
        return
    game.player_bombs -= 1
    game.bomb_timeout = datetime.now() + timedelta(seconds=0.7)
    tmp = shade_blast_flash(game, data['explosion_flashes'])
    for step, values in data['explosion_steps'].items():
        if step == 'five':
            for y_off, row in tmp:
                game.player_map[game.player_pos['y'] + y_off] = row
            update_screen(game, [game.player_pos['y'] + y_off for y_off in data['explosion_flashes']['radius_offset']])

        shade_radius(game, values)
        update_screen(game, [game.player_pos['y'] + y_off for y_off in range(-4, 5, 1)])
        time.sleep(0.048)


def shade_radius(game, step):
    for radius, color in list(zip(step['radius_offsets'], step['colors'])):
        for x_off, y_off in set(itertools.product(radius, repeat=2)) - {(0, 0)}:
            if game.map_coords.get((game.player_pos['y'] + y_off, game.player_pos['x'] + x_off), 'NaN') \
                    not in ['NaN', '⌂']:
                game.map_coords[(game.player_pos['y'] + y_off, game.player_pos['x'] + x_off)], \
                    game.player_map[game.player_pos['y'] + y_off][game.player_pos['x'] + x_off] = color, color


def shade_blast_flash(game, data):
    radius = data['radius_offset']
    before_flashed_slice = [(y_off, game.player_map[game.player_pos['y'] + y_off].copy()) for y_off in set(radius)
                            if game.map_coords.get((game.player_pos['y'] + y_off, game.player_pos['x'] + y_off), 'NaN')
                            != 'NaN']
    # TODO refactor
    for x_off, y_off in set(itertools.product(radius, repeat=2)) - {(0, 0)}:
        if game.map_coords.get((game.player_pos['y'] + y_off, game.player_pos['x'] + x_off), 'NaN') \
                not in ['NaN', '⌂']:
            game.player_map[game.player_pos['y'] + y_off][game.player_pos['x'] + x_off] = \
                colorama.Fore.WHITE + game.player_map[game.player_pos['y'] + y_off][game.player_pos['x'] + x_off] +\
                colorama.Fore.LIGHTBLACK_EX
    update_screen(game, [game.player_pos['y'] + y_off for y_off in radius])
    time.sleep(0.05)
    return before_flashed_slice


def clear_screen():
    print("\x1b[2J")


def move_cursor(y):
    print("\x1b[{};{}H".format(y + 1, 1))


def update_screen(game, y_rows=None):
    if y_rows == None:
        move_cursor(0)
        for row in game.player_map:
            rasterize(row)
    else:
        for row in y_rows:
            if game.map_coords.get((row, 0), 'NaN') != 'NaN':
                move_cursor(row)
                rasterize(game.player_map[row])


def rasterize(row):
    if '♫' in row:
        line_halved = "".join(row).split('♫')
        # TODO move to data
        print(str(colorama.Fore.LIGHTBLACK_EX + line_halved[0] + colorama.Fore.BLACK + colorama.Back.GREEN
                  + '♫' + colorama.Back.BLACK
                  + colorama.Fore.LIGHTBLACK_EX + line_halved[1]))
    else:
        print(colorama.Fore.LIGHTBLACK_EX + "".join(row))


def print_exit_screen(msg):
    print(colorama.Style.RESET_ALL)
    clear_screen()
    print_at_coords(msg, int((shutil.get_terminal_size()[1] - 2) / 3))

    if msg not in ['Game quit', 'Time ran out']:
        print_at_coords('Quitting in...')
        for i in range(4, 0, -1):
            print_at_coords(str(i))
            time.sleep(1)
        print_at_coords('Game quit')


def print_at_coords(msg, y=0, alignment='^'):
    print(y * '\n')
    print('{0:{1}{2}}'.format(msg, alignment, shutil.get_terminal_size()[0]))
