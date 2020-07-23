from abc import  ABC, abstractmethod
class shape ():
    @abstractmethod
    def printarea(self):
        return  0
class rectangle ():
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def area (self):
        return (self.length * self.width)
area = rectangle(9,6)
print(area.area())