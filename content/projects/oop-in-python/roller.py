# Graphics program to roll a pair of dice. Uses custom widgets
# Button and DieView

from random import randrange
from graphics import GraphWin, Point

from button import Button
from dieview import Dieview

def main():

	# create the application window
	win = GraphWin("Dice Roller")
	win.setCoords(0,0,10,10)
	win.setBackground("green2")

	# draw the interface widgets

	# event loop

	# close the window
	win.close()

main()
