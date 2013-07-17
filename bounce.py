import curses
import random

def bounce(stdscr):
    curses.curs_set(0)
    height, width = stdscr.getmaxyx()
    ypos, xpos = random.randrange(1, height - 2), random.randrange(1, width - 2)
    ydir, xdir = 1, 1
    stdscr.addstr(height//2, width//2, "Type a character")
    stdscr.nodelay(1)
    c = None
    while True:
        c = get_chr(stdscr) or c
        if not c:
            continue
#        stdscr.clear()
        if ypos in {0, height - 1}:
            ydir *= -1
        if xpos in {0, width - 1}:
            xdir *= -1
        ypos += ydir
        xpos += xdir
        stdscr.addstr(ypos, xpos, c)
        curses.delay_output(50)
        stdscr.refresh()


def get_chr(stdscr):
    try:
        c = stdscr.getkey()
    except curses.error:
        return None
    if c == 'q':
        exit(0)
    return c

if __name__ == '__main__':
    curses.wrapper(bounce)
