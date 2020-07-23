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


umar = employee ('umar',12,'FDC')
asfi = employee ('asfi',11,'FDC, ALM')
unu= employee.from_str('ubu-10-APS')


print (umar.printdetails())
print (asfi.printdetails())
print (umar.leaves)


