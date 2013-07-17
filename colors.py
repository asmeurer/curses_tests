import curses

def colors(stdscr):
    i = 0
    for name in dir(curses):
        if name.startswith("COLOR"):
            stdscr.addstr(i, 0, "%s " % name)
            stdscr.addstr("({0:04b}): ".format(getattr(curses, name)))
            stdscr.addstr("Example text", getattr(curses, name))
            i += 1

    stdscr.refresh()

    while True:
        c = stdscr.getch()
        if c == ord('q'):
            break

curses.wrapper(colors)
