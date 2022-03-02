# Kunal Shah
# Date 02/08/2022

# Problem 1

# importing math function
import math

# USing def to calculate area of circle using math.pi
def areaOfCircle(r):
    return math.pi * r * r

print(areaOfCircle(10))

# Problem 2

# prompt the user to enter a number
number = int(input('Enter a number to check in range(1, 10) : '))

# check if 'number' lies between 1 and 10
if number >= 1 and number <= 10:
    # if it is in range, print apt message
    print('The number is in range(1,10)')

else:
    # if it is NOT in range, print apt message
    print('The number is NOT in range(1,10)')


# Problem 3

my_List = [5, 2, 7, -1]

# find the sum of myList
list_Sum = sum(my_List)

# print the sum
print('\nSum of the list is ', list_Sum)


# Problem 4

# Using def
def unique_list(l):
  x = []
  # Usinf for loop to check
  for a in l:
    if a not in x:
      # using append function
      x.append(a)
  return x

print(unique_list([1, 3, 3, 3, 6, 2, 3, 5]))

# Problem 5

# import turtle library
import turtle


def drawSquare(t, sz):
    # draw four sides
    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()
alex = turtle.Turtle()

alex.color('blue')

# for square side and width
side = 20
width = 10
for squares in range(5):

    drawSquare(alex,side)
    #move pointer
    alex.penup()
    alex.back(width)
    alex.right(90)
    alex.forward(width)
    alex.left(90)
    alex.pendown()
    side+=2*width
wn.exitonclick()


# Problem 6

#import the turtle modules  
import turtle 
  
#Start a work Screen 
ws=turtle.Screen() 

#Define a Turtle Instance 
geekyTurtle=turtle.Turtle()

# to set the color 
geekyTurtle.color("pink")

# to set the size of lines
geekyTurtle.width(5)
  
#executing loop 10 times for 10 hexagones  
for j in range(10):
        # making 36  degree diffrence to create shape 
        geekyTurtle.left(36)
        #executing loop 6 times for 6 sides 
        for i in range(6): 
    
                #Move forward by 90 units  
                geekyTurtle.forward(90) 
    
                #Turn left the turtle by 300 degrees 
                geekyTurtle.left(300)
