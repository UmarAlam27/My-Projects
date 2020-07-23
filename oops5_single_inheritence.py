class employee:
    leaves=9
    def __init__(self, name, gradee,school):
        self.namee= name
        self.grade=gradee
        self.school=school
    def printdetails (self):
        return  f'The name is {self.namee}. The grade is {self.grade}. The school is {self.school}'
    @classmethod
    def from_str (cls, string):
        return cls(*string.split('-'))

    @staticmethod
    def goodprint (string):
        print ('This is good',string)

class programmer (employee): #SINGLE INHERITANCE  CONCEPT
    def __init__(self, name, gradee,school, language):
        self.namee= name
        self.grade=gradee
        self.school=school
        self.lanuage=language
    def printdetails (self):
        return  f'The name is {self.namee}. The grade is {self.grade}. The school is {self.school}. He knows {self.lanuage}languages'


umar = employee ('umar',12,'FDC')
asfi = employee ('asfi',11,'FDC, ALM')
raja= programmer ('raja', 8, 'APS', ['python', 'Cpp'])

print (umar.printdetails())
print (asfi.printdetails())
print (raja.printdetails())



