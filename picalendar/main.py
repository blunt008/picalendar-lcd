from time import sleep

import drivers

from quickstart import main as get_events


COLS = 16

def cli():
    """
    Display upcoming events on a 16x2 LCD
    """
    display = drivers.Lcd()
    events = get_events()
    try:
        while True:
            display_message(display, 1, events)
            sleep(5)
    except KeyboardInterrupt:
        display.lcd_clear()


def display_message(display: drivers.Lcd, row: int, events: list) -> None:
    """
    Display message on LCD
    Split message if it's longer than 16 columns
    """
    for event in events:
        message = event.get("summary", "")
        start = event.get("start", "")
        display.lcd_display_string(f"{start}", 1)
        if len(message) > COLS:
            for i in range(0, len(message), COLS):
                text_to_show = message[i: i + COLS].lstrip()
                if len(text_to_show) < COLS:
                    difference = COLS - len(text_to_show)
                    text_to_show = text_to_show + " " * difference
                display.lcd_display_string(text_to_show, 2)
                sleep(2)
        else:
            if len(message) < COLS:
                difference = COLS - len(message)
                message = message + " " * difference
            display.lcd_display_string(message, 2)
            sleep(2)


if __name__ == "__main__":
    cli()