class A :
    def __init__(self,b1,b2):
        self.b1=b1
        self.b2=b2
    def bb (self):
        return f'Name is {self.b1}. Pak is {self.b2}'
    def __add__(self, other): #add dunder, similarly from internet search different 'Mapping operators to functions'
        return  self.b2 + other.b2
    def __truediv__(self, other): #divide dunder, similarly from internet search different 'Mapping operators to functions'
        return  self.b2 / other.b2
    def __pow__(self, other): #exponential dunder, similarly from internet search different 'Mapping operators to functions'
        return  self.b2 ** other.b2


a= A('umar', 17013)
b= A('asfi', 16958)
#print (a.bb())
#print (b.bb())
print (a + b) #add dunder
print (a / b) #divide dunder
print (a ** b) #divide dunder


