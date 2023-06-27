#Hope you have read readme file before this. Now, just think like, we have a turtle named alex and its tail was dipped in a paint. 

#when it moves anywhere through the window, its tail is touching down. Right? 
#Therefore when alex.forward(10) will make our tutle move 10 pixel forward and its tail is touching on the screen... 
#therefore we can see the the way it moved 10 pixel away from its current postion

#so if we say alex.color("red") the paint on its tail become red.Now lets see more.
import turtle
wn = turtle.Screen()      # creates a graphics window
alex = turtle.Turtle()    # create a turtle named alex
alex.color("blue")        # make alex in blue color
alex.pensize(3)           # Set alex's width
alex.forward(150)         # tell alex to move forward by 150 units
alex.left(90)             # turn by 90 degrees
alex.forward(75)          

#we can up our turtle's tail. So that the paint wont printed while moving.
alex.up()                # pen up or turtle's tail is up
alex.forward(100)        # this move alex, but no line is drawn
alex.down()              # put down the pen. Next moements of turtle will be visible



alex.shape("turtle")     #we can change the shape of tutle. by default it is an arrow. Here we changed it into turtle shape. We can have "blank","circle","square"etc.

alex.speed(10)#we can control the speed of tutle movement. alex.speed(0) will not show any animations.
wn.exitonclick()     #wait for a user click on the canvas to exit.
