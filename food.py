import turtle
import random
from square import Square

__version__ = '1.0.0'
__author__ = 'Oleksii Polovyi'

class Food:
	"""This class creates food for Snake game"""
	def __init__(self, pen):
		"""Constructor for Food class. This funcion is called upon 
		initialization. It saves a Square object and list of colors 
		as a class members.
		Parameters
		----------
		None
		Returns
		-------
		None
		"""
		self.pen = pen
		self.square = Square(self.pen)
		self.colors = ["red","green","yellow","blue","magenta", "cyan"]
	
	def create_food(self):
		"""Create a random food location for the self.square.
		Parameters
		----------
		None
		Returns
		-------
		None
		"""
		self.square.x = random.randint(-self.square.size,self.square.size) * self.square.size
		self.square.y = random.randint(-self.square.size,self.square.size) * self.square.size
		self.draw_food()

	def collision_with_food(self,x,y):
		"""Checks if snake has food collision.
		Returns True if it is and False otherwise.
		Parameters
		----------
		x : int
			Horizontal coordinate
		y : int
			Vertical coordinate
		Returns
		-------
		Bool
			True -  when there is a collision
			False - when there is none
		"""
		if self.square.x == x and self.square.y == y:
			return True
		else:
			return False
		
	def draw_food(self):
		"""Draw food using Square.
		Parameters
		----------
		None
		Returns
		-------
		None
		"""
		self.pen.clear()
		turtle.tracer(0,0)
		self.square.draw(self.square.x,self.square.y,random.choice(self.colors))
		turtle.tracer(40,0)

if __name__ == '__main__':
	food = Food(turtle.Turtle())
	screen = turtle.Screen()
	screen.onkey(lambda : food.create_food(), "space")
	screen.listen()
	screen.mainloop()

