import curses
import curses.textpad

def textpad(stdscr):
    curses.textpad.rectangle(stdscr, 0, 0, 20, 50)
    win = curses.newwin(19, 49, 1, 1)

    textbox = curses.textpad.Textbox(win)
    stdscr.refresh()
    textbox.edit()
    get_q(stdscr)

def get_q(stdscr):
    while True:
        c = stdscr.getch()
        if c == ord('q'):
            break

if __name__ == '__main__':
    curses.wrapper(textpad)
