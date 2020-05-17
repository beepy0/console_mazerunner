import keyboard
import time
import colorama
import shutil
import random
from static.data import instructions, Direction, keyboard_to_direction, game_ending_text, city_elements

player_map = []
player_pos = {'x': 1, 'y': 1}
map_coords = {}


def init_level():
    for line in range(shutil.get_terminal_size()[1] - 2):
        player_map.append([])
        for cell in range(shutil.get_terminal_size()[0] - 1):
            if line > shutil.get_terminal_size()[1] - 12 and cell > shutil.get_terminal_size()[0] - 25:
                player_map[line].append(' ')
                continue
            player_map[line].append(' ' if random.randint(0, 10) < 8 else random.choice(city_elements))
    player_map[-5][-12] = '⌂'

    player_map[player_pos['y']][player_pos['x']] = '♫'
    for row_ind, line in enumerate(player_map):
        for col_ind, cell in enumerate(line):
            map_coords[(row_ind, col_ind)] = cell


def move_one_step(directions):
    if directions == [Direction.SAME, Direction.SAME]:
        return
    next_step = map_coords.get((player_pos['y'] + directions[0].value, player_pos['x'] + directions[1].value),
                               'out of bounds')
    if next_step == ' ':
        # reset current map board and its coordinates
        map_coords[(player_pos['y'], player_pos['x'])], player_map[player_pos['y']][player_pos['x']] = ' ', ' '
        # get player's new position
        player_pos['y'], player_pos['x'] = player_pos['y'] + directions[0].value, player_pos['x'] + directions[1].value
        # update current map board and its coordinates with new player position
        map_coords[(player_pos['y'], player_pos['x'])], player_map[player_pos['y']][player_pos['x']] = '♫', '♫'

        update_screen()
    elif next_step == '⌂':
        print_exit_screen(game_ending_text)


def clear_screen():
    print ("\x1b[2J")


def update_screen():
    # moves the console cursor to the starting position
    move_cursor(0, 0)
    print_map()


def move_cursor(x, y):
    print ("\x1b[{};{}H".format(y+1, x+1))


def print_map():
    for row in player_map:
        if '♫' in row:
            line_halved = "".join(row).split('♫')
            print(colorama.Fore.LIGHTBLACK_EX + line_halved[0] + colorama.Fore.BLACK + colorama.Back.GREEN
                  + '♫' + colorama.Style.RESET_ALL
                  + colorama.Fore.LIGHTBLACK_EX + line_halved[1])
        else:
            print(colorama.Fore.LIGHTBLACK_EX + "".join(row))


def print_exit_screen(text):
    print(colorama.Style.RESET_ALL)
    clear_screen()
    print_at_coords(text, int((shutil.get_terminal_size()[1] - 2) / 3))

    if text != 'Game quit':
        print_at_coords('Quitting in...')
        for i in range(4, 0, -1):
            print_at_coords(str(i))
            time.sleep(1)
        print_at_coords('Just kidding, press escape to quit!')


def print_at_coords(text, y=0):
    print(y * '\n')
    print('{:^{}}'.format(text, shutil.get_terminal_size()[0]))


if __name__ == '__main__':
    init_level()
    colorama.init()

    clear_screen()
    print(instructions)
    keyboard.wait('s')

    print_map()
    keyboard.on_press(lambda _: move_one_step(
        keyboard_to_direction.get(keyboard.get_hotkey_name(), [Direction.SAME, Direction.SAME])))

    keyboard.wait('esc')
    print_exit_screen('Game quit')
