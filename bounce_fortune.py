"""
Display a fortune in a cool way

Requires the `fortune` command to be installed.
"""
import curses
import random
import subprocess

def main(stdscr):
    curses.curs_set(0)
    bounce_fortune(stdscr)

    while True:
        c = get_chr(stdscr)
        if c:
            stdscr.clear()
            bounce_fortune(stdscr)


def bounce_fortune(stdscr):
    height, width = stdscr.getmaxyx()
    ypos, xpos = random.randrange(0, height - 1), random.randrange(0, width - 1)
    ydir, xdir = random.choice([-1, 1]), random.choice([-1, 1])
    stdscr.nodelay(1)
    c = None
    fortune = get_fortune()

    for c in fortune:
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

def get_fortune():
    p = subprocess.Popen(['fortune', '-s'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = p.communicate()
    r = p.returncode
    if r or not output[0]:
        if output[1]:
            raise RuntimeError("fortune did not work: " + output[1])
        raise RuntimeError("fortune did not work. Maybe it isn't installed?")
    return ' '.join(output[0].strip().split('\n'))

if __name__ == '__main__':
    curses.wrapper(main)
