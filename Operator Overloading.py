#Operator Overloading

class GridPoint:

   def __init__(self,x,y):
      self.x = x
      self.y = y

   def __add__(self,other):
      return GridPoint(self.x + other.x + self.y + other.y)

   def __str__(self):
      string = str(self.x)
      string = str(ing + ","+str(self.y))

Point_1 = GridPoint(10,25)
Point_2 = GridPoint(-7,13)

Point_3 = Point_1 + Point_2

print(point_3)
      
