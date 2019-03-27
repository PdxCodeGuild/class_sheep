import curses
from curses import wrapper
import time
import sys

intro = "The year is 3281.\nBla bla bla.\n"
for letter in intro:
    time.sleep(.2)
    print(letter, end='', flush=True)
time.sleep(4)

#def main(stdscr):
#    stdscr.clear()
#    while True:
#        # Store the key value in the variable `c`
#        c = stdscr.getch()
#        # Clear the terminal
#        stdscr.clear()
#        if c == ord('a'):
#            stdscr.addstr("You pressed the 'a' key.")
#        elif c == curses.KEY_UP:
#            stdscr.addstr("You pressed the up arrow.")
#        else:
#            stdscr.addstr("This program doesn't know that key.....")

def main(stdscr):
    # Make stdscr.getch non-blocking
    stdscr.nodelay(True)
    stdscr.clear()
    width = 4
    count = 0
    direction = 1
    while True:
        c = stdscr.getch()
        # Clear out anything else the user has typed in
        curses.flushinp()
        stdscr.clear()
        # If the user presses p, increase the width of the springy bar
        if c == ord('p'):
            width += 1
        # Draw a springy bar
        stdscr.addstr("#" * count)
        count += direction
        if count == width:
            direction = -1
        elif count == 0:
            direction = 1
        # Wait 1/10 of a second. Read below to learn about how to avoid
        # problems with using time.sleep with getch!
        time.sleep(0.1)

#begin_x = 20; begin_y = 7
#height = 5; width = 40
#win = curses.newwin(height, width, begin_y, begin_x)

# Ends application

def teardown():
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

wrapper(main)
