import curses
import curses.ascii

def main(stdscr):
    curses.curs_set(0)

    display_txt(stdscr)

def display_txt(stdscr):
    height, width = stdscr.getmaxyx()
    while True:
        c = get_ch(stdscr)
        if not c:
            continue
        for i in range(height):
            stdscr.addstr(i, 0, c*(width - 1))
        stdscr.refresh()

def get_ch(stdscr):
    try:
        c = stdscr.getkey()
    except curses.error:
        return None
    if curses.ascii.isprint(c):
        return c

if __name__ == '__main__':
    curses.wrapper(main)
