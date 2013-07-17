import curses

def colors(stdscr):
    colors = {getattr(curses, name): name for name in dir(curses) if
        name.startswith("COLOR_")}

    if not curses.can_change_color():
        curses.addstr("Sorry, your terminal doesn't support color awesomeness")
        stdscr.refresh()
        get_q()
        return

    

    stdscr.refresh()

def get_q():
    while True:
        c = stdscr.getch()
        if c == ord('q'):
            break

curses.wrapper(colors)
