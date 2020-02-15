#abstract class

from abc import ABC

class polygon(ABC):
    
    #abstract method
    def noofsoides(self):
        pass

    def calculate_area(self):
        pass

class triangle(polygon):
    
    #overriding abstract method
    def noofsides(self):
        print("I have 3 sides")

    def calculate_area(self,height,breadth):
        a1=1/2*height*breadth
        print("area of triangle",a1)

class rectangle(polygon):
    
    #overriding abstract method
    def noofsides(self):
        print("I have 4 sides")

    def calculate_area(self,length,breadth)
        a2=length*breadth
        print("area of rectangle is",a2)

class square(polygon):
    
    #overriding abstract method
    def noofsides(self,side):
        a3=side**2
        print("I have 6 sides")
        print("area of square is",a3)

class circle(polygon):
    
    #overriding abstract method
    def noofsides(self,r):
        a4=3.14*r*r
        print("area of cricle is",a4)

#driver code
R=triangle()
R.noofsides(4,5)

k=rectangle()
k.noofsides(5,4)

R=square()
R.noofsides(3)

k=circle()
k.noofsides(4)
