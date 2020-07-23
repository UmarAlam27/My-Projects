class employee:
    leaves=9 #Public Specifier
    _leaves=15 #Protected Specifier - that can be used in
    __leaves=19 #
    def __init__(self, name, gradee,school):
        self.namee= name
        self.grade=gradee
        self.school=school
    def printdetails (self):
        return  f'The name is {self.namee}. The grade is {self.grade}. The school is {self.school}'

class programmer:
    def __init__(self, name, gradee,school, language):
        self.namee= name
        self.grade=gradee
        self.school=school
        self.lanuage=language
    def printdetails (self):
        return  f'The name is {self.namee}. The grade is {self.grade}. The school is {self.school}. He knows {self.lanuage}languages'

class player (employee, programmer):
    leaves=13
    def __init__(self, name, gradee,school, language, sports):
        self.namee= name
        self.grade=gradee
        self.school=school
        self.lanuage=language
        self.sports=sports
    def printdetails (self):
        return  f'The name is {self.namee}. The grade is {self.grade}. The school is {self.school}. He knows {self.lanuage}languages. He plays {self.sports}'


tim=player('tim','olevels', 'Beacon House', 'C++', 'Cricket')
print (tim.leaves)
print (tim._leaves)

print (tim._employee__leaves)#syntax very important for private specifier




