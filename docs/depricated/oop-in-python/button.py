import graphics 

class Button:
    """ A button is a labeled rectangle in a window. It is activated or deactivated
    with the activate() and deactivate() methods. The clicked (p) method returns
    true if the button is active and p is inside it. """

    def __init__ (self, win, center, width, height, label):
        """ creates a rectangualr button, eg:
        my_button = Button (my_window, center_point, width, height, 'quit')"""

        #set attributes here

    def clicked(self, point):
        """returns True if the button active and point is inside
        """

        #CODE

    def get_label(self):
        """returns the label string of the button"""

        #CODE

    def activate(self):
        """Sets this button to 'active'"""

        #CODE

    def deactivate (self):
        """Sets this button to 'active'"""

        #CODE
