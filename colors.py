import curses

def colors(stdscr):
    colors = {getattr(curses, name): name for name in dir(curses) if
        name.startswith("COLOR_")}

    stdscr.addstr(str(curses.can_change_color()))

    stdscr.refresh()

    while True:
        c = stdscr.getch()
        if c == ord('q'):
            break

curses.wrapper(colors)
