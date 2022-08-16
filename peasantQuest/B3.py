#!/usr/bin/env python3

import curses


def peasantHome():

    curses.initscr()
    win = curses.newwin(30,60,1,1)
    win.keypad(True)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)

    win.refresh()

    heroImg = '#'
    hero = [0,20]

    win.addch(hero[0], hero[1], heroImg)

    close_screen = False

    while not close_screen: 
        event = win.getch()
        win.clear()
        win.refresh()
        
