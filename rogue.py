#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:35:05 2019

@author: cicero
"""

import curses as crs

class Entity():
    '''
    superclass for all entities in the game
    under construction
    '''
    pass

class Mobile(Entity):
    '''
    superclass for all moving objects
    appear with spawn coordinates and character
    provide move method to enable motion
    provide draw method to redraw self at new position
    '''
    def __init__(self, spawn_y, spawn_x, char, window):
        self.y = spawn_y
        self.x = spawn_x
        self.char = char
        self.window = window
        self.draw()
    
    def draw(self):
        self.window.addstr(self.y, self.x, self.char)
    
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
    #TODO subclass this from Mobile when possible
    pass


def main(window):
    extent = window.getmaxyx()
    maxy = extent[0]
    maxx = extent[1]
    player = Mobile(maxy//2,maxx//2,'@',window)
    running = True
    while running:
        key = window.getch()
        #window.addstr(10,10,chr(key)) <debug>
        if key == 27: #ESC
            running = False
            break
        else:
            player.move(key)
    return 0


if __name__ == "__main__":
    crs.wrapper(main)
    