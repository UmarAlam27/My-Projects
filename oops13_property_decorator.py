class A:
    def __init__(self, firstname, secondname, thirdname):
        self.firstname=firstname
        self.secondname=secondname

    def printout (self):
        return  f'My name is {self.firstname} {self.secondname}. '
    @property #when this decorator is used, in print, we dont need brackets to have output
    def email (self):
        return f' Email is {self.firstname}{self.secondname}@yahoo.com'

a= A ('Umar', 'Farooq', 'kingsgmail.com')
print (a.printout())
a.firstname= 'asfi'
print (a.printout())
#print (a.email())
print (a.email) # brackets not required once 'property' decorator is used


