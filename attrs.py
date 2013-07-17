import curses

def highlighting(stdscr):
    i = 0
    for name in dir(curses):
        if name.startswith("A_"):
            stdscr.addstr(i, 0, "%s " % name)
            stdscr.addstr("({0:b}): ".format(getattr(curses, name)))
            stdscr.addstr("Example text", getattr(curses, name))
            i += 1

    stdscr.refresh()

    while True:
        c = stdscr.getch()
        if c == ord('q'):
            break

curses.wrapper(highlighting)
