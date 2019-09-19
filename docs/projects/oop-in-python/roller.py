# Graphics program to roll a pair of dice. Uses custom widgets
# Button and DieView

from random import randrange
from graphics import GraphWin, Point

from button import Button
from die_view import Dieview

def main():

	# create the application window
	window = GraphWin("Dice Roller")
	window.setCoords(0,0,10,10)
	window.setBackground("green2")

	# draw the interface widgets

	# event loop

	# close the window
	window.close()

if __name__ == '__main__': # This kind of thing is considered "good practice". 
	                       # Can you figure out why?
	main()
