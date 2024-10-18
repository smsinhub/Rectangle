class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}
        
    def area(self):
        print("Area of Rectangle is:",self.length*self.width)
    def perimeter(self):
        print("Perimeter of Rectangle is:",self.length+self.width*2)
    
rect = Rectangle(int(input()),int(input()))
for i in rect :
    print(i)
rect.area()
rect.perimeter()



    
