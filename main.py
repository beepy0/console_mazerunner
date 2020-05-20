# coding: utf-8
import keyboard
import colorama
import time
import sys
import platform
import atexit
import cursor
from assets.game import Game, clear_screen, update_screen, print_at_coords, print_exit_screen
from assets.data import Instructions, keyboard_to_direction
from datetime import datetime


def toggle_console_echo(fd, enabled):
    (iflag, oflag, cflag, lflag, ispeed, ospeed, cc) \
        = termios.tcgetattr(fd)

    if enabled:
        lflag |= termios.ECHO
    else:
        lflag &= ~termios.ECHO

    new_attr = [iflag, oflag, cflag, lflag, ispeed, ospeed, cc]
    termios.tcsetattr(fd, termios.TCSANOW, new_attr)


if __name__ == '__main__':
    cursor.hide()
    # disable console echo on unix-based systems (Linux/OS X)
    if platform.system() in ['Linux', 'Darwin']:
        import termios
        atexit.register(toggle_console_echo, sys.stdin.fileno(), enabled=True)
        toggle_console_echo(sys.stdin.fileno(), enabled=False)

    game = Game()
    game.init_level()
    colorama.init()

    clear_screen()
    for line in game.instructions:
        print_at_coords(line, alignment='<')
    keyboard.wait('s')

    print_at_coords(game.begin_screen_text)
    time.sleep(2)
    game.start_time = datetime.now()

    update_screen(game)
    keyboard.on_press(lambda _: game.process_keypress(
        keyboard_to_direction.get(keyboard.get_hotkey_name(), [Instructions.SAME, Instructions.SAME])))

    game.wait_quit('esc')
    print_exit_screen(game.exit_screen_text)

