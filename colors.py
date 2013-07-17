import curses

def colors(stdscr):
    colors = {getattr(curses, name): name for name in dir(curses) if
        name.startswith("COLOR_")}

    stdscr.addstr(0, 0, "Press c")
    for backnum in range(1, 8):
        backcolor = colors[backnum]
        for forenum in range(1, 8):
            forecolor = colors[forenum]
            curses.init_pair(forenum, forenum, backnum)
            stdscr.addstr(forenum, 0, "%s on %s" % (forecolor, backcolor),
                curses.color_pair(forenum))
        stdscr.refresh()
        get_c(stdscr)

    stdscr.addstr(0, 0, "Press q")
    get_q(stdscr)

def get_q(stdscr):
    while True:
        c = stdscr.getch()
        if c == ord('q'):
            break

def get_c(stdscr):
    while True:
        c = stdscr.getch()
        if c == ord('c'):
            break

if __name__ == '__main__':
    curses.wrapper(colors)
