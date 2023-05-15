# File: mg_ICA3_C.py
# A short summary of the program
#
#   Pseudocode:
#   1) Creates a graphics window
#   2) Takes in 7 user inputs (mouse clicks) to create a simple house
#       2.a) The 1st & 2nd clicks are opposite corners of a pink rectangle frame
#       2.b) The 3rd click indicates the center of the top edge of a red rectangular door
#       2.c) The 4th click indicates the center of a yellow circular door knob
#       2.d) The 5th & 6th clicks indicate the centers of the square windows (orange and blue)
#       2.e) The 7th (last) click indicates the peake of a black triangular roof
#   3) Once the mouse is clicked again after drawing the roof the graphics window closes
#
# by: Michael Gerber

import graphics
from graphics import*

def main():

    win = GraphWin("Let's Design a House",500,500)

    message = Text(Point(250,485),'Click on lower left corner of your house frame')             # creates initial instruction message
    message.setSize(11)                                                                         # sets font size to 11
    message.draw(win)                                                                           # displays initial instruction message

    for i in range(1,8):
        
        click = win.getMouse()                                                                  # gets user input (mouse click)
        message.undraw()                                                                        # delete instruction message
        
        if (i == 1):           
            # House Frame 
            lower = Point(click.getX(),click.getY())                                            # lower click location
            message = Text(Point(250,485),'Click on upper right corner of your house frame')    # updates instruction message            
        if (i == 2):      
            upper = Point(click.getX(),click.getY())                                            # upper click location   
            houseFrame = Rectangle(lower,upper)                                                 # creates house frame
            houseWidth = upper.getX() - lower.getX()                                            # width of house frame
            houseFrame.setFill('pink')                                                          # fills house frame pink
            houseFrame.draw(win)                                                                # displays the house frame 
            message = Text(Point(250,485),'Click on the center of the top of the door')         # updates instruction message           
        if (i == 3):
            # Door 
            doorWidth = houseWidth / 5                                                          # width of door
            doorLowerXY = Point(click.getX() - (doorWidth/2),lower.getY())                      # lower left corner of door
            doorUpperXY = Point(click.getX() + (doorWidth/2),click.getY())                      # upper right corner of door
            door = Rectangle(doorLowerXY,doorUpperXY)                                           # creates door
            door.setFill('red')                                                                 # fills the door red
            door.draw(win)                                                                      # displays the door
            message = Text(Point(250,485),'Click on the center of the door knob')               # updates instruction message      
        if (i == 4):
            # Door Knob 
            doorKnob = Circle(Point(click.getX(),click.getY()),doorWidth/12)                    # creates door knob
            doorKnob.setFill('yellow')                                                          # fills door knob yellow
            doorKnob.draw(win)                                                                  # displays door knob
            message = Text(Point(250,485),'Click on the center of the first window')            # updates instruction message
        if (i == 5):
            # Window 1
            windowWidth = doorWidth / 2                                                         # width of window
            window1LowerXY = Point(click.getX() - windowWidth/2,click.getY() + windowWidth/2)   # lower left corner of window 1
            window1UpperXY = Point(click.getX() + windowWidth/2,click.getY() - windowWidth/2)   # upper right corner of window 1
            window1 = Rectangle(window1LowerXY,window1UpperXY)                                  # creates window 1
            window1.setFill('orange')                                                           # fills window 1 orange
            window1.draw(win)                                                                   # displays window 1
            message = Text(Point(250,485),'Click on the center of the second window')           # updates instruction message
        if (i == 6):
            # Window 2
            window2LowerXY = Point(click.getX() - windowWidth/2,click.getY() + windowWidth/2)   # lower left corner of window 2
            window2UpperXY = Point(click.getX() + windowWidth/2,click.getY() - windowWidth/2)   # upper right corner of window 2
            window2 = Rectangle(window2LowerXY,window2UpperXY)                                  # creates window 2
            window2.setFill('blue')                                                             # fills window 2 blue
            window2.draw(win)                                                                   # displays window 2
            message = Text(Point(250,485),'Click on the peak of the roof')                      # updates instruction message
        if (i == 7):
            # Roof
            left = Point(lower.getX(),upper.getY())                                             # left base point of roof
            right = upper                                                                       # right base point of roof
            peak = Point(click.getX(),click.getY())                                             # peak of the roof
            roof = Polygon(left,right,peak)                                                     # creates the roof
            roof.setFill('black')                                                               # fills the roof black
            roof.draw(win)                                                                      # displays the roof
            message = Text(Point(250,485),'Click again to quit!')                               # updates instruction message to a quit message

        message.setSize(11)                                                                     # sets font size to 11    
        message.draw(win)                                                                       # displays the updated instruction message
    
    if (win.getMouse()):                                                                        # if mouse is clicked again close the graphics window
        win.close()  
    
main()
