# File: mg_ICA3_B.py
# A short summary of the program
#
#   Pseudocode:
#   1) Creates a graphics window 
#   2) Displays an x-y graph in the window
#   3) Takes user input as two mouse clicks in the x-y graph to be used for endpoints of a line
#   4) Following the two clicks a line is drawn between the two points
#   5) Information about the line is then calculated and displayed (length & slope)
#   6) Once the mouse is clicked again the graphics window closes
#
# by: Michael Gerber

import graphics
from graphics import*

def main():
    
#   Graphics Window
    win = GraphWin('Line Segment Info',400,400)     # creates a 400 x 400 graphics window 'Click and Move'

#   x-y Axes
    xAxis = Line(Point(50,200),Point(350,200))      # creates an x-axis
    xAxis.setArrow("both")                          # creates arrows on both ends of the x-axis
    yAxis = Line(Point(200,50),Point(200,350))      # creates a y-axis
    yAxis.setArrow("both")                          # creates arrows on both ends of the y-axis
    xAxis.draw(win)                                 # displays x-axis
    yAxis.draw(win)                                 # displays y-axis
    
#   Endpoints of x-Axis
    xLeft = Text(Point(50,212),'-10')               # creates x-axis left endpoint
    xRight = Text(Point(350,212),'10')              # creates x-axis right endpoint
    xLeft.setSize(12)                               # sets font size
    xRight.setSize(12)                              # sets font size
    xLeft.draw(win)                                 # displays left endpoint
    xRight.draw(win)                                # displays right endpoint
    
#   Endpoints of y-Axis
    yBottom = Text(Point(200,362),'-10')            # creates y-axis bottom endpoint
    yTop = Text(Point(200,38),'10')                 # creates y-axis top endpoint
    yBottom.setSize(12)                             # sets font size
    yTop.setSize(12)                                # sets font size
    yBottom.draw(win)                               # displays bottom endpoint
    yTop.draw(win)                                  # displays top endpoint

#   Origin
    origin = Text(Point(210,210),'0')               # creates origin
    origin.setSize(12)                              # sets font size
    origin.draw(win)                                # displays origin

#   Message
    message = Text(Point(200,15),'Click on endpoints of a line segment.')
    message.draw(win)
 
#   Line
    click1 = win.getMouse()                         # gets first user input (mouse click)
    click2 = win.getMouse()                         # gets second user input (mouse click)
    lin = Line(click1,click2)                       # creates a line connecting the two points
    lin.draw(win)                                   # displays line
  
#   Midpoint
    midPoint = lin.getCenter()                      # returns a clone of the midpoint of the line segment
    midPoint.setFill('red')                         # sets the midpoint color to red
    midPoint.draw(win)                              # displays a midpoint

#   Length/Slope        
    x1 = (click1.getX() / 15) - 13                                      # get position of x1 on [-10,10]
    x2 = (click2.getX() / 15) - 13                                      # get position of x2 on [-10,10]
    y1 = -((click1.getY() / 15) - 13)                                   # get position of y1 on [-10,10]
    y2 = -((click2.getY() / 15) - 13)                                   # get position of y2 on [-10,10]
    leng = round((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1/2),2)      # calculates length
    slope = round((y2 - y1) / (x2 - x1),2)                              # calculates slope

    newMessage = Text(Point(200,15),'Length:                Slope:   ') # creates a new message with length and slope information
    lengthMessage = Text(Point(186,15),leng)                            # creates a new message with length info
    slopeMessage = Text(Point(296,15),slope)                            # creates a new message with slope info
    message.undraw()                                                    # deletes old top message
    newMessage.draw(win)                                                # displays new top message
    lengthMessage.draw(win)                                             # displays length message
    slopeMessage.draw(win)                                              # displays slope message
    
#   Quit Message
    quitMessage = Text(Point(200,385),"Click again to quit!")           # creates quit message
    quitMessage.draw(win)                                               # displays the message on the graphics window

    if (win.getMouse()):
        win.close()                                 # closes graphics window following another mouse click

main()
