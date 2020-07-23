class A:
    def __init__(self, firstname, secondname, thirdname):
        self.firstname=firstname
        self.secondname=secondname

    def printout (self):
        return  f'My name is {self.firstname} {self.secondname}. '
    @property #when this decorator is used, in print, we dont need brackets to have output

    def email (self):
        return f' Email is {self.firstname}{self.secondname}@yahoo.com'

    @email.setter #to change email we need to use setters
    def email (self,string):

        names=string.split('@')[0]
        self.firstname=names.split('.')[0]
        self.secondname=names.split('.')[1]


a= A ('Umar', 'Farooq', 'kingsgmail.com')
print (a.printout())
a.firstname= 'asfi'
print (a.printout())
#print (a.email())
print (a.email) # brackets not required once 'property' decorator is used

a.email= 'this.that@yahoo.com' #error - cant set this attribute, to set this attribute we use setters
print (a.email)

