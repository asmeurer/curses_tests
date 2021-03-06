import time
import curses

def pad_example(stdscr):
    pad = curses.newpad(100, 100)
    #  These loops fill the pad with letters; this is
    # explained in the next section
    for y in range(0, 100):
        for x in range(0, 100):
            try: pad.addch(y,x, ord('a') + (x*x+y*y) % 26 )
            except curses.error: pass

    #  Displays a section of the pad in the middle of the screen
    pad.refresh( 0,0, 5,5, 20,75)
    time.sleep(10)

if __name__ == '__main__':
    curses.wrapper(pad_example)
