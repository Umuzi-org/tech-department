import graphics

class DieView:
	"""DieView is a widget that displays a graphical representation of a 
	standard six-sided die."""

	def __init__(self, window, center, size):
		""" create a view of a die e.g: d1 = DieView (myWin, graphics.Point(40,50), 20).
		This creates a die centered at (40,50) with length 20. """

		# define standard values for drawing the die
		self.window = window 		# for drawing the pips
		self.background = "white"	# colour of die face
		self.foreground = "black"	# colour of pips
		self.pip_size = 0.1 * size 	# radius of each pip
		hsize = size/2				# half the size of the die
		offset = 0.6 * hsize		# distance from centre to outer pips

		# create a square for the face

		# create 7 circles for standard pip locations

		# Draw an initial value

	def _make_pip(self, x, y):
		""" Internal helper method to draw a pip at (x,y)"""
		#CODE

	def set_value(self, value):
		"""Set this die to display value. """

		# turn all pips off

		# turn correct pips on
