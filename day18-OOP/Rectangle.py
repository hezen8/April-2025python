class Rectangle:
    def __init__(self,l,w):# 1st function its running  the function
        self.length=l
        self.width=w
    def calc_Area(self):
        return self.length*self.width
    
    def calc_perimeter(self):
        return ((self.length+self.width)*2)
    