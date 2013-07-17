import curses
import curses.ascii
from bounce_fortune import get_fortune

def main(stdscr):
    curses.curs_set(0)

    display_txt(stdscr)

def display_txt(stdscr):
    height, width = stdscr.getmaxyx()
    fortune = get_fortune()
    for c in fortune:
        if not curses.ascii.isprint(c):
            continue
        for i in range(height):
            stdscr.addstr(i, 0, c*(width - 1))
        stdscr.refresh()
        curses.delay_output(200)

def get_ch(stdscr):
    try:
        c = stdscr.getkey()
    except curses.error:
        return None
    if curses.ascii.isprint(c):
        return c

if __name__ == '__main__':
    curses.wrapper(main)
