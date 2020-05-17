import keyboard
import colorama
import time
from assets.game import Game, clear_screen, print_map, print_at_coords, print_exit_screen
from assets.data import Direction, keyboard_to_direction
from datetime import datetime


if __name__ == '__main__':
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

    print_map(game)
    keyboard.on_press(lambda _: game.move_one_step(
        keyboard_to_direction.get(keyboard.get_hotkey_name(), [Direction.SAME, Direction.SAME])))

    game.wait_quit('esc')
    print_exit_screen(game.exit_screen_text)
