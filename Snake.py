#SNAKE GAME


class Cell:
  def __init__(self,t):
    # set initial position
    self.x = 0
    self.y = 0
    # set initial size of a cell
    self.cell_size = 10
    # set the turtle
    self.t = t
  
  # draw a square at (x,y) of color
  def draw_cell(self,x,y,color):
    # update cell information
    self.set_cell(x,y)
    # move to (x,y)
    self.t.penup()
    self.t.goto(self.x,self.y)
    self.t.pendown()
    # set the color
    self.t.color(color)
    # draw the square
    self.t.begin_fill()
    for i in range(4):
      self.t.fd(self.cell_size)
      self.t.left(90)
    self.t.end_fill()
  
  # update coordinates of the cell
  def set_cell(self, x, y):
    self.x = x
    self.y = y
    
class Food:
  def __init__ (self):
    self.t=turtle.Turtle()
    self.t.hidetrurle()
    self.t.speed(0)
    self.cell=Cell(self.t)
  def random_food(self):
    self.cell.x=random.randint(-200,200)
    self.cell.y=random.randint(-200,200)
  def draw_square(self, colour):
    for i in range(4):
      t.fd(self.cell.size)
      t.left((90)
      self.clear()
  def food_collision(self):
    if self.cell.x ==x and y == self.cell.y:
       return True
    else:
       return False
             
 class Game:
    def __init__ (self):
      self.screen.onkey(lambda: self.snake.set_direction("Up"), "Up")
      self.screen.onkey(lambda: self.snake.set_direction("Left"), "Left")
      self.screen.onkey(lambda: self.snake.set_direction("Down"), "Down")
      self.screen.onkey(lambda: self.snake.set_direction("Right"), "Right")
      self.screen.listen()
  
     game = Game()
      

