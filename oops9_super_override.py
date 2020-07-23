varB= 'Universal'
class A1:
    varB = 'I m in class A'

    def __init__(self):
        # super ().__init__()
        self.varB = 'Hi Umar'
        self.varC = 'ABC DEF GHI'


class A (A1):
    varB='I m in class A'

    def __init__(self):
        # super ().__init__()
        self.varB = 'Hi'
        self.varC = 'ABC'
        super ().__init__()

class B (A, A1):
     varB= 'I m in class B'
     def __init__(self):
        #super ().__init__() #use and position (locati) of this function is important
        self.varB= 'self . var B function of class B'
        super().__init__() #use and position (locati) of this function is important
        self.varC='ABC DEF'
        #super().__init__() #use and position (locati) of this function is important
    #pass

a= A ()
b= B ()
print (b.varB, b.varC, varB)