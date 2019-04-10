#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:35:05 2019

@author: cicero
"""

import curses as crs

class MapEntity():
    '''
    superclass for all entities that can appear on a map.
    stores fields for appearance and location, and a method for drawing onto
    the screen.
    '''
    def __init__(self, window, char, spawn_y, spawn_x):
        self.window = window
        self.char = char
        self.y = spawn_y
        self.x = spawn_x
        
            
    def draw(self):
        self.window.addstr(self.y, self.x, self.char)
        

class Mobile(MapEntity):
    '''
    subclasses all fields from MapEntity; adds move method to enable motion
    '''
    def __init__(self, *args):
        super().__init__(*args)
        
    def move(self, direction):
        if direction == crs.KEY_UP:
            self.y -= 1
        elif direction == crs.KEY_DOWN:
            self.y += 1
        elif direction == crs.KEY_RIGHT:
            self.x += 1
        elif direction == crs.KEY_LEFT:
            self.x -= 1
        self.draw()


class Player(Mobile):
    '''
    special case of Mobile object; fixed appearance and is_player boolean for
    future use in collision detection.
    '''
    def __init__(self, window):
        super().__init__(window, '@', 10, 10)
        self.is_player = True
        

def main(window):
    maxy = window.getmaxyx()[0]
    maxx = window.getmaxyx()[1]
    player = Mobile(maxy//2, maxx//2, '@', window)
    running = True
    while running:
        key = window.getch()
        #window.addstr(10,10,chr(key)) <debug>
        if key == 27: #ESC_key
            running = False
            break
        else:
            player.move(key)
            continue
    return 0


if __name__ == "__main__":
    crs.wrapper(main)
    