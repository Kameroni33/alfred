import time

import controls
import display


def run():
    # Print the screen
    display.print_screen()
    controls.prompt_user_input()
    time.sleep(0.1)


if __name__ == '__main__':
    display = display.Display()
    controls = controls.Controls(display)
    while True:
        run()
