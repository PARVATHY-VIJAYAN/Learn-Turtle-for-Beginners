# Learn-Turtle-for-Beginners
Here I will introduce a module that allows us to create a data object called a turtle that can be used to draw pictures and different shapes using certain functions like forward(), right(), left() etc.
<ul>
<li>
  Here are some basic methods:
 <ul>
    <li>left()</li>
  	<li>right()</li>
  	<li>forward()</li>
 </ul>
</li>
<li>Attributes:
	<ul>
    <li>color -default black</li>
  	<li>bgcolor</li>
  	<li>heading</li>
  	<li>position - 0,0</li>
  	<li>pensize(width)</li>
</li>
</ul>

<br>

Now just understand what these methods does:
left(90) ---> means our virtual turtle will turn 90 degrees to left from its current position which is considered as 0 degrees.
right(90) ---> means our virtual turtle will turn 90 degrees to right from its current position.
forward(150)---> means our virtual turtle will move forward 150 pixel
<hr>

Now understand the code given below :

import turtle             # allows us to use the turtles library.This line imports the module called turtle, which has all the built in functions for drawing on the screen with the Turtle object.
wn = turtle.Screen()      # creates a graphics window
alex = turtle.Turtle()    # create a turtle named alex
alex.forward(150)         # tell alex to move forward by 150 units
alex.left(90)             # turn by 90 degrees
alex.forward(75)          #  tell alex to move forward by 75 units

<hr>
<i>Turtle starts out facing east.</i>
<hr>

 Ok guys now run the above code to understand more functions and attributes of turtle library.
