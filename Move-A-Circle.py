# File: mg_ICA3_A.py
# A short summary of the program
#
#   Pseudocode:
#   1) Creates a graphics window
#   2) Draws an orange circle to the middle of the graphics window
#   3) Takes in user input as mouse clicks and moves the circle to the location of the click
#   4) After 7 clicks, displays a message "click again to quit!"
#   5) The program closes following the next click
#
# by: Michael Gerber

import graphics
from graphics import *

def main():
    
    win = GraphWin('Click and Move',400,400)    # creates a 400 x 400 graphics window 'Click and Move'
    win.setBackground('blue')                   # sets the window background blue

    p = Point(200,200)                          # creates a point in the middle of the window
    circ = Circle(p,25)                         # creates a circle using the given point p and a radius
    circ.draw(win)                              # draws the circle to the graphics window
    circ.setFill('orange')                      # fills the circle orange

    for i in range(1,8):                        # iterates 7 times
        p = win.getMouse()                      # gets location of the mouse click
        circ.undraw()                           # deletes the original circle
        circ = Circle(p,25)                     # sets circle in new location (mouse click)
        circ.setFill('orange')                  # fills circle orange
        circ.draw(win)                          # draws new circle to graphics window
        
    p = Point(200,350)                          # creates point to be used for text location
    message = Text(p,"Click again to quit!")    # creates message at location p with given text
    message.setTextColor('white')               # sets textColor white
    message.draw(win)                           # displays the message on the graphics window

    if (win.getMouse()):
        win.close()                             # closes graphics window following another mouse click
    
main()
